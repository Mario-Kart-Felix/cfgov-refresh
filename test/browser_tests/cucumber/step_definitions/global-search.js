'use strict';

const BASE_JS_PATH = '../../../../cfgov/unprocessed/js/';
const breakpointsConfig = require( BASE_JS_PATH + 'config/breakpoints-config' );
const chai = require( 'chai' );
const chaiAsPromised = require( 'chai-as-promised' );
const { defineSupportCode } = require( 'cucumber' );
const { expect } = require( 'chai' );
const { shouldShouldnt } = require( '../../util/index.js' );

const BASE_SEL = '.m-global-search';
const TRIGGER_SEL = BASE_SEL + ' [data-js-hook="behavior_flyout-menu_trigger"]';
const CONTENT_SEL = BASE_SEL + ' [data-js-hook="behavior_flyout-menu_content"]';
const INPUT_SEL = BASE_SEL + ' input#query';
const SEARCH_SEL = BASE_SEL + ' [data-js-hook="behavior_flyout-menu_content"] .btn';
const CLEAR_SEL = BASE_SEL + ' .input-contains-label_after';
const SUGGEST_SEL = BASE_SEL + ' .m-global-search_content-suggestions';
const EC = protractor.ExpectedConditions;

let _dom;
let _nonLinkDom;

chai.use( chaiAsPromised );

defineSupportCode( function( { Then, When, Before } ) {

  Before( function() {
    _nonLinkDom = element( by.css( '.o-footer_official-website' ) );
    _dom = {
      trigger:   element( by.css( TRIGGER_SEL ) ),
      content:   element( by.css( CONTENT_SEL ) ),
      input:     element( by.css( INPUT_SEL ) ),
      searchBtn: element( by.css( SEARCH_SEL ) ),
      clearBtn:  element( by.css( CLEAR_SEL ) ),
      suggest:   element( by.css( SUGGEST_SEL ) )
    };
  } );

  When( 'I click on the search molecule',
    function() {

      return _dom.trigger.click();
    }
  );

  When( /I enter "(.*)" in the search molecule/,
    function( searchText ) {
      _dom.trigger.click();

      return _dom.input.sendKeys( searchText );
    }
  );

  When( 'I click off the search molecule',
    function( ) {


      return _dom.trigger.click()
             .then( _nonLinkDom.click );
    }
  );

  When( 'I focus on the search molecule trigger',
    function( ) {

      return _dom.trigger.sendKeys( protractor.Key.SPACE );
    }
  );

  When( 'I perform tab actions on the search molecule',
    function( ) {
      var activeElement = browser.driver.switchTo().activeElement();
      activeElement.sendKeys( protractor.Key.TAB );
      activeElement = browser.driver.switchTo().activeElement();

      return activeElement.sendKeys( protractor.Key.TAB );
    }
  );

  Then( /it (should|shouldn't) have a clear button label/,
    function( shouldHaveLabel ) {

      return expect( _dom.clearBtn.isDisplayed() )
             .to.eventually
             .equal( shouldShouldnt( shouldHaveLabel ) );
    }
  );

  Then( 'it should focus the search input field',
    function( ) {
      var activeElement = browser
                          .driver
                          .switchTo()
                          .activeElement()
                          .getAttribute( 'id' );

      return activeElement
            .then( attributeId =>
              expect( _dom.input.getAttribute( 'id' ) )
              .to.eventually
              .equal( attributeId )
            );
    }
  );

  Then( /the search molecule (should|shouldn't) have a search trigger/,
    function( shouldHaveTrigger ) {
      let expectedCondition;

      if ( shouldShouldnt( shouldHaveTrigger ) ) {
        expectedCondition = EC.elementToBeClickable( _dom.trigger );
      } else {
        expectedCondition = EC.not( EC.elementToBeClickable( _dom.trigger ) );
      }

      return browser.wait( expectedCondition )
             .then( () =>
               expect( _dom.trigger.isDisplayed() )
               .to.eventually
               .equal( shouldShouldnt( shouldHaveTrigger ) )
             );
    }
  );

  Then( /it (should|shouldn't) have search input content/,
    function( shouldHaveInput ) {
      let expectedCondition;

      if ( shouldShouldnt( shouldHaveInput ) ) {
        expectedCondition = EC.elementToBeClickable( _dom.content );
      } else {
        expectedCondition = EC.not( EC.elementToBeClickable( _dom.content ) );
      }

      return browser.wait( expectedCondition )
             .then( () =>
                expect( _dom.content.isDisplayed() )
                .to.eventually
                .equal( shouldShouldnt( shouldHaveInput ) )
              );
    }
  );

  Then( 'I should navigate to search portal',
    function( ) {

      return browser.wait( EC.visibilityOf( _dom.searchBtn ) )
             .then( () => {
               const portalUrl =
                 'https://search.consumerfinance.gov/' +
                 'search?utf8=%E2%9C%93&affiliate=cfpb&query=test';

               _dom.searchBtn.click();

               return expect( browser.getCurrentUrl() )
                      .to.eventually
                      .equal( portalUrl );
             } );
    }
  );

  Then( /it (should|shouldn't) have suggested search terms/,

    function( shouldHaveTerms ) {

      return expect( _dom.suggest.isDisplayed() )
             .to.eventually
             .equal( shouldShouldnt( shouldHaveTerms ) );
    }
  );


  Then( 'should have suggested search terms',

    function( ) {

      return expect( _dom.suggest.isDisplayed() )
             .to.eventually
             .equal( true );
    }
  );

} );
