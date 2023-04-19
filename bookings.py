import requests
import csv
from bs4 import BeautifulSoup


fieldnames = [
    "Hotel_Name",
    "Double Room",
    "Triple Room",
    "Deluxe Single Room",
    "Deluxe Double Room",
    "Family Room",
    "Double Room with Terrace",
    "Double or Twin Room",
    "Economy Twin Room",
    "Twin Room",
    "Quadruple Room",
    "Standard Triple Room",
    "Superior Double or Twin Room",
    "Family Room with Bathroom",
    "Twin Room with Shared Bathroom",
    "Double Room with Private Bathroom",
    "Triple Room with Shared Bathroom",
    "Triple Room with Private Bathroom",
    "Quadruple Room with Private Bathroom",
    "Double Room with Private External Bathroom",
    "King Studio with Sofa Bed",
    "Double or Twin Room with Extra Bed",
    "Penthouse Apartment",
    "Superior Apartment",
    "Deluxe Apartment",
    "Standard Twin Room",
    "Standard Double Room",
    "Standard Double or Twin Room",
    "Standard Quadruple Room",
    "Classic Triple Room",
    "Classic Quadruple Room",
    "Superior Family Room",
    "Single Room",
    "Triple Room with Shower",
    "Suite",
    "Standard Suite",
    "Superior Suite",
    "Studio",
    "Tent",
    "Studio (2 Adults)",
    "Deluxe Two-Bedrooms Apartment with Fireplace",
    "Superior Double Room with Garden View",
    "Superior Triple Room with Garden View",
    "Superior Double Room with Sofa and with Garden View",
    "Standard Quadruple Room with Kitchenette",
    "Star_Rating",
    "Address",
]

cookies = {
    "px_init": "0",
    "bkng_sso_session": "e30",
    "cors_js": "1",
    "OptanonConsent": "implicitConsentCountry=nonGDPR&implicitConsentDate=1681743126414",
    "_gid": "GA1.2.1780790249.1681743127",
    "BJS": "-",
    "_pxvid": "6c31855f-dd2f-11ed-a917-4e68496f4d4b",
    "_gcl_au": "1.1.112323773.1681743130",
    "_scid": "229df030-2f68-4bd0-b156-7063f0145941",
    "_pin_unauth": "dWlkPU16Y3dNbVF6T0dNdE1tWTBOaTAwWTJSa0xUazVZakV0TXprek5XWm1ZV014WWprMw",
    "_sctr": "1%7C1681671600000",
    "b": "%7B%22countLang%22%3A4%7D",
    "_gac_UA-116109-18": "1.1681744759.CjwKCAjw3POhBhBQEiwAqTCuBoX_51XaQoBEeU_vfDuKDmXAjW8jLEbT8R7tq1wdrJL6KpXQsfNA4xoC4DEQAvD_BwE",
    "_gcl_aw": "GCL.1681744761.CjwKCAjw3POhBhBQEiwAqTCuBoX_51XaQoBEeU_vfDuKDmXAjW8jLEbT8R7tq1wdrJL6KpXQsfNA4xoC4DEQAvD_BwE",
    "bkng_sso_ses": "eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6IjhzQXVjY1d5TERtc2Z5Qkx0MmRoRDVoSTk2Y1l6bUs3M0t2a09KSm5QckkifV19",
    "bkng_sso_auth": "CAIQARqEATEvPMc6AHwUEZvMw4J/8YklCkAg36aw5sLRh/H86hPARPQzeLVq/nBP5sTaXqr07pN2Ab1Mmi5R19Dv5D1jt0BN/JDzhkghfxoBBnu5V/XdrPyRvfXLgTGbi59fPQZ3vnaq6U5BXUQXBNsblbmPI1CPeF9Ru3TDPkOxycvKo4wnQ2Pe6g==",
    "bkng_sso_auth_1681832614": "CAIQARqEATEvPMc6AHwUEZvMw4J/8YklCkAg36aw5sLRh/H86hPARPQzeLVq/nBP5sTaXqr07pN2Ab1Mmi5R19Dv5D1jt0BN/JDzhkghfxoBBnu5V/XdrPyRvfXLgTGbi59fPQZ3vnaq6U5BXUQXBNsblbmPI1CPeF9Ru3TDPkOxycvKo4wnQ2Pe6g==",
    "_gat": "1",
    "pxcts": "ca12cab0-ddff-11ed-9fb5-7a696b416e65",
    "_pxff_ddtc": "1",
    "_pxhd": "m46ietwzHE0KPFcO%2FW8mTbqqF%2FcyHaDRq0EXc51i8O7gVmsl6vUyiTHTNhi7Us33okAykNXiLzHhvbNgAdwo6w%3D%3D%3AfmGY7mxZ1hNe3x07dauU-Ne2oBr8cGPiIFZUUXCkWC69duHocPv0KFdHymel2PP1Y2enqA8SeESGeV7eUDyj-JZYB6TGpE7AnKCRsXA216o%3D",
    "bkng_prue": "1",
    "_px3": "adb602733cd22f49c2d64d68868debac19299e9c19ef0620987e00c9a1bc0d23:r35ZAQ25+X1DOvng8W8TYSnm4RGOhUoRvbc4wk2KT0cEz88n2dHiWLxWOqllGfZQOI82NAPCIhvDPndl4R5d4g==:1000:kWPPI+L3NyJp73We5hHQ6ET8OZ6X719kp8iKqdU4W7jJzyMuuW9mp7Y3WdXJRyPreXvMk06r0hJETeM2CTR1FzdzE+OM48k/W4Lrmb6ZKmfxDUgCi9N27vdmwFEjg1Pu4zeQJHDQ0fBq3/+cHqrY2VNIJjrT5dypLHHMZPL+LZ3MRK4l+rUsIy/1R0EuWpYPCk5HjiJ1gwvHZ+XF/NawJA==",
    "_pxde": "8f5793fbd744f9b43780df4496a4fd5b38f9b54be9bcaec7f96813f954411ecd:eyJ0aW1lc3RhbXAiOjE2ODE4MzI2NDg5NTAsImZfa2IiOjAsImlwY19pZCI6W119",
    "_scid_r": "229df030-2f68-4bd0-b156-7063f0145941",
    "_ga": "GA1.1.713886904.1681743127",
    "_ga_FPD6YLJCJ7": "GS1.1.1681832620.2.1.1681832649.0.0.0",
    "_uetsid": "6e37b7a0dd2f11edbcd7b5787f5f4105",
    "_uetvid": "bd8565c043f911edaa654360921b70d6",
    "_derived_epik": "dj0yJnU9X0FmQnJVQlJUTEM2UkhkYXprOGNBTmRjNHVnNDJrT18mbj01emVYa3Vwei1rejdzSTZZbnNKWENBJm09OCZ0PUFBQUFBR1EtdXNvJnJtPTgmcnQ9QUFBQUFHUS11c28mc3A9Mg",
    "g_state": '{"i_p":1681919052255,"i_l":2}',
    "bkng": "11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbiKbS0JOgDBLjuBR%2BQVyLAVqsCqaC8eVsC1NXNQ5eQtj6UaFBVfXjA4m8p0Fm%2Fd%2F6caK5X2vFVL52IoPywqmkGMNxb0WoLuwbckWkx9hSo7nGqKNRJv6f2rzjJxEdiDucit8xME0O%2FWBimPZZZiDTwc%2FjkcQLdojfDrjg0yR%2BWfc%3D",
    "lastSeen": "0",
    "11_srd": "%7B%22features%22%3A%5B%7B%22id%22%3A9%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D",
}

headers = {
    "authority": "www.booking.com",
    "accept": "*/*",
    "accept-language": "en,ru;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.booking.com",
    "referer": "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEZyAEM2AEB6AEBiAIBqAIDuAKn9fqhBsACAdICJDk5NjkxYzcxLWM1ZGMtNDkyMC1hYTMzLWViODA3MmY2YzQ0NtgCBeACAQ&sid=17bbe3350ba8fd3998e8883df7bb3fdc&aid=304142&ss=Tyr%C5%A1ova+2063%2C+256+01+Bene%C5%A1ov%2C+Czechia&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=ChIJ_7n6aKF_DEcR05yp2VBIra0&dest_type=region&place_id=ChIJ_7n6aKF_DEcR05yp2VBIra0&latitude=49.7811316&longitude=14.6841122&ac_position=0&ac_click_type=g&ac_langcode=en-gb&ac_suggestion_list_length=1&search_selected=true&search_pageview_id=ab7f6e9378f704fe&checkin=2023-06-25&checkout=2023-06-30&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=0",
    "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.906 (beta) Yowser/2.5 Safari/537.36",
    "x-booking-context-action-name": "searchresults_irene",
    "x-booking-context-aid": "304142",
    "x-booking-csrf-token": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTY4MTgzMjY0MSwiZXhwIjoxNjgxOTE5MDQxfQ.rqtq4eekVhyt6-XRa_BDsTv-ucJ0hLme8h21BgjReyp01pOenGDzIE4e9ultw92LQVNPXH8TcJJWG-gVcR3iLQ",
    "x-booking-et-serialized-state": "Ee_Ift6ZNC-gFxciPM3efAnmxPtJ0FxCzOFgG8x2BZXWsWJubQi_Ee_isl4m-xJWs",
    "x-booking-pageview-id": "6fe36ea005070425",
    "x-booking-site-type-id": "1",
    "x-booking-topic": "capla_browser_b-search-web-searchresults",
}

page_names = []

with open("hotels-database-sample.csv", "r") as file:
    data = csv.DictReader(file)
    for col in data:
        params = {
            "ss": col["full_address"] + "," + col["country"],
            "label": "gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEZyAEM2AEB6AEBiAIBqAIDuAKn9fqhBsACAdICJDk5NjkxYzcxLWM1ZGMtNDkyMC1hYTMzLWViODA3MmY2YzQ0NtgCBeACAQ",
            "sid": "17bbe3350ba8fd3998e8883df7bb3fdc",
            "aid": "304142",
            "lang": "en-gb",
            "sb": "1",
            "src_elem": "sb",
            "src": "index",
            "dest_id": "ChIJ_7n6aKF_DEcR05yp2VBIra0",
            "dest_type": "region",
            "place_id": "ChIJ_7n6aKF_DEcR05yp2VBIra0",
            "latitude": col["latitude"],
            "longitude": col["longitude"],
            "ac_position": "0",
            "ac_click_type": "g",
            "ac_langcode": "en-gb",
            "ac_suggestion_list_length": "1",
            "search_selected": "true",
            "search_pageview_id": "ab7f6e9378f704fe",
            "checkin": "2023-06-25",
            "checkout": "2023-06-30",
            "group_adults": "2",
            "no_rooms": "1",
            "group_children": "0",
            "sb_travel_purpose": "leisure",
        }

        json_data = {
            "operationName": "FullSearch",
            "variables": {
                "input": {
                    "acidCarouselContext": None,
                    "childrenAges": [],
                    "dates": {
                        "checkin": "2023-06-25",
                        "checkout": "2023-06-30",
                    },
                    "doAvailabilityCheck": False,
                    "encodedAutocompleteMeta": None,
                    "enableCampaigns": True,
                    "filters": {},
                    "forcedBlocks": None,
                    "location": {
                        "searchString": col["full_address"] + "," + col["country"],
                        "destType": "LATLONG",
                        "latitude": float(col["latitude"]),
                        "longitude": float(col["longitude"]),
                    },
                    "metaContext": None,
                    "nbRooms": 1,
                    "nbAdults": 2,
                    "nbChildren": 0,
                    "showAparthotelAsHotel": True,
                    "needsRoomsMatch": False,
                    "sbCalendarOpen": False,
                    "optionalFeatures": {
                        "forceArpExperiments": True,
                        "testProperties": False,
                    },
                    "pagination": {
                        "rowsPerPage": 25,
                        "offset": 0,
                    },
                    "rawQueryForSession": f"/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaLUBiAEBmAEJuAEZyAEM2AEB6AEBiAIBqAIDuAKn9fqhBsACAdICJDk5NjkxYzcxLWM1ZGMtNDkyMC1hYTMzLWViODA3MmY2YzQ0NtgCBeACAQ&sid=17bbe3350ba8fd3998e8883df7bb3fdc&aid=304142&ss={params['ss']}&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=ChIJ_7n6aKF_DEcR05yp2VBIra0&dest_type=region&place_id=ChIJ_7n6aKF_DEcR05yp2VBIra0&latitude=49.7811316&longitude=14.6841122&ac_position=0&ac_click_type=g&ac_langcode=en-gb&ac_suggestion_list_length=1&search_selected=true&search_pageview_id=ab7f6e9378f704fe&checkin=2023-06-25&checkout=2023-06-30&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=0",
                    "referrerBlock": {
                        "clickPosition": 0,
                        "clickType": "g",
                        "blockName": "autocomplete",
                    },
                    "sorters": {
                        "selectedSorter": None,
                        "referenceGeoId": None,
                        "tripTypeIntentId": None,
                    },
                    "travelPurpose": 2,
                    "seoThemeIds": [],
                    "useSearchParamsFromSession": True,
                },
                "geniusVipUI": {
                    "enableEnroll": True,
                    "page": "SEARCH_RESULTS",
                },
            },
            "extensions": {},
            "query": "query FullSearch($input: SearchQueryInput!, $geniusVipUI: GeniusVipUIsInput) {\n  searchQueries {\n    search(input: $input) {\n      ...FullSearchFragment\n      __typename\n    }\n    __typename\n  }\n  geniusVipEnrolledProgram(input: $geniusVipUI) {\n    ...geniusVipEnrolledProgramFragment\n    __typename\n  }\n}\n\nfragment FullSearchFragment on SearchQueryOutput {\n  banners {\n    ...Banner\n    __typename\n  }\n  breadcrumbs {\n    ... on SearchResultsBreadcrumb {\n      ...SearchResultsBreadcrumb\n      __typename\n    }\n    ... on LandingPageBreadcrumb {\n      ...LandingPageBreadcrumb\n      __typename\n    }\n    __typename\n  }\n  carousels {\n    ...Carousel\n    __typename\n  }\n  destinationLocation {\n    ...DestinationLocation\n    __typename\n  }\n  entireHomesSearchEnabled\n  filters {\n    ...FilterData\n    __typename\n  }\n  recommendedFilterOptions {\n    ...FilterOption\n    __typename\n  }\n  pagination {\n    nbResultsPerPage\n    nbResultsTotal\n    __typename\n  }\n  tripTypes {\n    ...TripTypesData\n    __typename\n  }\n  results {\n    ...BasicPropertyData\n    ...MatchingUnitConfigurations\n    ...PropertyBlocks\n    ...BookerExperienceData\n    priceDisplayInfo {\n      ...PriceDisplayInfo\n      __typename\n    }\n    priceDisplayInfoIrene {\n      ...PriceDisplayInfoIrene\n      __typename\n    }\n    licenseDetails {\n      nextToHotelName\n      __typename\n    }\n    __typename\n  }\n  searchMeta {\n    ...SearchMetadata\n    __typename\n  }\n  sorters {\n    option {\n      ...SorterFields\n      __typename\n    }\n    __typename\n  }\n  oneOfThreeDeal {\n    ...OneOfThreeDeal\n    __typename\n  }\n  zeroResultsSection {\n    ...ZeroResultsSection\n    __typename\n  }\n  __typename\n}\n\nfragment BasicPropertyData on SearchResultProperty {\n  acceptsWalletCredit\n  basicPropertyData {\n    accommodationTypeId\n    id\n    isTestProperty\n    location {\n      address\n      city\n      countryCode\n      __typename\n    }\n    pageName\n    ufi\n    photos {\n      main {\n        highResUrl {\n          relativeUrl\n          __typename\n        }\n        lowResUrl {\n          relativeUrl\n          __typename\n        }\n        highResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        lowResJpegUrl {\n          relativeUrl\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    reviewScore: reviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      showScore\n      secondaryScore\n      secondaryTextTag {\n        translation\n        __typename\n      }\n      showSecondaryScore\n      __typename\n    }\n    externalReviewScore: externalReviews {\n      score: totalScore\n      reviewCount: reviewsCount\n      showScore\n      totalScoreTextTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    starRating {\n      value\n      symbol\n      caption {\n        translation\n        __typename\n      }\n      tocLink {\n        translation\n        __typename\n      }\n      showAdditionalInfoIcon\n      __typename\n    }\n    isClosed\n    paymentConfig {\n      installments {\n        minPriceFormatted\n        maxAcceptCount\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  badges {\n    caption {\n      translation\n      __typename\n    }\n    closedFacilities {\n      startDate\n      endDate\n      __typename\n    }\n    __typename\n  }\n  customBadges {\n    showIsWorkFriendly\n    showParkAndFly\n    showSkiToDoor\n    showBhTravelCreditBadge\n    showOnlineCheckinBadge\n    __typename\n  }\n  description {\n    text\n    __typename\n  }\n  displayName {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  geniusInfo {\n    benefitsCommunication {\n      header {\n        title\n        __typename\n      }\n      items {\n        title\n        __typename\n      }\n      __typename\n    }\n    geniusBenefits\n    geniusBenefitsData {\n      hotelCardHasFreeBreakfast\n      hotelCardHasFreeRoomUpgrade\n      sortedBenefits\n      __typename\n    }\n    showGeniusRateBadge\n    __typename\n  }\n  isInCompanyBudget\n  location {\n    displayLocation\n    mainDistance\n    publicTransportDistanceDescription\n    skiLiftDistance\n    beachDistance\n    nearbyBeachNames\n    beachWalkingTime\n    geoDistanceMeters\n    __typename\n  }\n  mealPlanIncluded {\n    mealPlanType\n    text\n    __typename\n  }\n  persuasion {\n    autoextended\n    geniusRateAvailable\n    highlighted\n    preferred\n    preferredPlus\n    showNativeAdLabel\n    nativeAdId\n    nativeAdsCpc\n    nativeAdsTracking\n    bookedXTimesMessage\n    __typename\n  }\n  policies {\n    showFreeCancellation\n    showNoPrepayment\n    enableJapaneseUsersSpecialCase\n    __typename\n  }\n  ribbon {\n    ribbonType\n    text\n    __typename\n  }\n  recommendedDate {\n    checkin\n    checkout\n    lengthOfStay\n    __typename\n  }\n  showGeniusLoginMessage\n  showPrivateHostMessage\n  soldOutInfo {\n    isSoldOut\n    messages {\n      text\n      __typename\n    }\n    alternativeDatesMessages {\n      text\n      __typename\n    }\n    __typename\n  }\n  nbWishlists\n  visibilityBoosterEnabled\n  showAdLabel\n  isNewlyOpened\n  propertySustainability {\n    isSustainable\n    tier {\n      type\n      __typename\n    }\n    facilities {\n      id\n      __typename\n    }\n    certifications {\n      name\n      __typename\n    }\n    chainProgrammes {\n      chainName\n      programmeName\n      __typename\n    }\n    levelId\n    __typename\n  }\n  seoThemes {\n    caption\n    __typename\n  }\n  relocationMode {\n    distanceToCityCenterKm\n    distanceToCityCenterMiles\n    distanceToOriginalHotelKm\n    distanceToOriginalHotelMiles\n    phoneNumber\n    __typename\n  }\n  bundleRatesAvailable\n  recommendedDatesLabel\n  __typename\n}\n\nfragment Banner on Banner {\n  name\n  type\n  isDismissible\n  showAfterDismissedDuration\n  position\n  requestAlternativeDates\n  title {\n    text\n    __typename\n  }\n  imageUrl\n  paragraphs {\n    text\n    __typename\n  }\n  metadata {\n    key\n    value\n    __typename\n  }\n  pendingReviewInfo {\n    propertyPhoto {\n      lowResUrl {\n        relativeUrl\n        __typename\n      }\n      lowResJpegUrl {\n        relativeUrl\n        __typename\n      }\n      __typename\n    }\n    propertyName\n    urlAccessCode\n    __typename\n  }\n  nbDeals\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  secondaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  iconName\n  flexibleFilterOptions {\n    optionId\n    filterName\n    __typename\n  }\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  __typename\n}\n\nfragment Carousel on Carousel {\n  aggregatedCountsByFilterId\n  carouselId\n  position\n  contentType\n  hotelId\n  name\n  soldoutProperties\n  priority\n  themeId\n  title {\n    text\n    __typename\n  }\n  slides {\n    captionText {\n      text\n      __typename\n    }\n    name\n    photoUrl\n    subtitle {\n      text\n      __typename\n    }\n    type\n    title {\n      text\n      __typename\n    }\n    action {\n      context {\n        key\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DestinationLocation on DestinationLocation {\n  name {\n    text\n    __typename\n  }\n  inName {\n    text\n    __typename\n  }\n  countryCode\n  __typename\n}\n\nfragment FilterData on Filter {\n  trackOnView {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  trackOnClick {\n    type\n    experimentHash\n    value\n    __typename\n  }\n  name\n  field\n  category\n  filterStyle\n  title {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  subtitle\n  options {\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnViewPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelectPopular {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    ...FilterOption\n    __typename\n  }\n  filterLayout {\n    isCollapsable\n    collapsedCount\n    __typename\n  }\n  stepperOptions {\n    min\n    max\n    default\n    selected\n    title {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    field\n    labels {\n      text\n      translationTag {\n        translation\n        __typename\n      }\n      __typename\n    }\n    trackOnView {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClick {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDeSelect {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnClickIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnDecrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    trackOnIncrease {\n      type\n      experimentHash\n      value\n      __typename\n    }\n    __typename\n  }\n  sliderOptions {\n    min\n    max\n    minSelected\n    maxSelected\n    minPriceStep\n    minSelectedFormatted\n    currency\n    histogram\n    selectedRange {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment FilterOption on Option {\n  optionId: id\n  count\n  selected\n  urlId\n  additionalLabel {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  value {\n    text\n    translationTag {\n      translation\n      __typename\n    }\n    __typename\n  }\n  starRating {\n    value\n    symbol\n    caption {\n      translation\n      __typename\n    }\n    showAdditionalInfoIcon\n    __typename\n  }\n  __typename\n}\n\nfragment LandingPageBreadcrumb on LandingPageBreadcrumb {\n  destType\n  name\n  urlParts\n  __typename\n}\n\nfragment MatchingUnitConfigurations on SearchResultProperty {\n  matchingUnitConfigurations {\n    commonConfiguration {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    unitConfigurations {\n      name\n      unitId\n      bedConfigurations {\n        beds {\n          count\n          type\n          __typename\n        }\n        nbAllBeds\n        __typename\n      }\n      apartmentRooms {\n        config {\n          roomId: id\n          roomType\n          bedTypeId\n          bedCount: count\n          __typename\n        }\n        roomName: tag {\n          tag\n          translation\n          __typename\n        }\n        __typename\n      }\n      nbAllBeds\n      nbBathrooms\n      nbBedrooms\n      nbKitchens\n      nbLivingrooms\n      nbUnits\n      unitTypeNames {\n        translation\n        __typename\n      }\n      localizedArea {\n        localizedArea\n        unit\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PropertyBlocks on SearchResultProperty {\n  blocks {\n    blockId {\n      roomId\n      occupancy\n      policyGroupId\n      packageId\n      mealPlanId\n      __typename\n    }\n    finalPrice {\n      amount\n      currency\n      __typename\n    }\n    originalPrice {\n      amount\n      currency\n      __typename\n    }\n    onlyXLeftMessage {\n      tag\n      variables {\n        key\n        value\n        __typename\n      }\n      translation\n      __typename\n    }\n    freeCancellationUntil\n    hasCrib\n    blockMatchTags {\n      childStaysForFree\n      __typename\n    }\n    thirdPartyInventoryContext {\n      isTpiBlock\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceDisplayInfo on PriceDisplayInfo {\n  badges {\n    name {\n      translation\n      __typename\n    }\n    tooltip {\n      translation\n      __typename\n    }\n    style\n    identifier\n    __typename\n  }\n  chargesInfo {\n    translation\n    __typename\n  }\n  displayPrice {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  priceBeforeDiscount {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  rewards {\n    rewardsList {\n      termsAndConditions\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      breakdown {\n        productType\n        amountPerStay {\n          amount\n          amountRounded\n          amountUnformatted\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    rewardsAggregated {\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      copy {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  useRoundedAmount\n  discounts {\n    amount {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    name {\n      translation\n      __typename\n    }\n    description {\n      translation\n      __typename\n    }\n    itemType\n    __typename\n  }\n  excludedCharges {\n    excludeChargesAggregated {\n      copy {\n        translation\n        __typename\n      }\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    excludeChargesList {\n      chargeMode\n      chargeInclusion\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  taxExceptions {\n    shortDescription {\n      translation\n      __typename\n    }\n    longDescription {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment PriceDisplayInfoIrene on PriceDisplayInfoIrene {\n  badges {\n    name {\n      translation\n      __typename\n    }\n    tooltip {\n      translation\n      __typename\n    }\n    style\n    identifier\n    __typename\n  }\n  chargesInfo {\n    translation\n    __typename\n  }\n  displayPrice {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  priceBeforeDiscount {\n    copy {\n      translation\n      __typename\n    }\n    amountPerStay {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    __typename\n  }\n  rewards {\n    rewardsList {\n      termsAndConditions\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      breakdown {\n        productType\n        amountPerStay {\n          amount\n          amountRounded\n          amountUnformatted\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    rewardsAggregated {\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      copy {\n        translation\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  useRoundedAmount\n  discounts {\n    amount {\n      amount\n      amountRounded\n      amountUnformatted\n      currency\n      __typename\n    }\n    name {\n      translation\n      __typename\n    }\n    description {\n      translation\n      __typename\n    }\n    itemType\n    productId\n    __typename\n  }\n  excludedCharges {\n    excludeChargesAggregated {\n      copy {\n        translation\n        __typename\n      }\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    excludeChargesList {\n      chargeMode\n      chargeInclusion\n      chargeType\n      amountPerStay {\n        amount\n        amountRounded\n        amountUnformatted\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  taxExceptions {\n    shortDescription {\n      translation\n      __typename\n    }\n    longDescription {\n      translation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment BookerExperienceData on SearchResultProperty {\n  bookerExperienceContentUIComponentProps {\n    ... on BookerExperienceContentLoyaltyBadgeListProps {\n      badges {\n        variant\n        key\n        title\n        popover\n        logoSrc\n        logoAlt\n        __typename\n      }\n      __typename\n    }\n    ... on BookerExperienceContentFinancialBadgeProps {\n      paymentMethod\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SearchMetadata on SearchMeta {\n  availabilityInfo {\n    hasLowAvailability\n    unavailabilityPercent\n    totalAvailableNotAutoextended\n    __typename\n  }\n  boundingBoxes {\n    swLat\n    swLon\n    neLat\n    neLon\n    type\n    __typename\n  }\n  childrenAges\n  dates {\n    checkin\n    checkout\n    lengthOfStayInDays\n    __typename\n  }\n  destId\n  destType\n  maxLengthOfStayInDays\n  nbRooms\n  nbAdults\n  nbChildren\n  userHasSelectedFilters\n  customerValueStatus\n  affiliatePartnerChannelId\n  affiliateVerticalType\n  __typename\n}\n\nfragment SearchResultsBreadcrumb on SearchResultsBreadcrumb {\n  destId\n  destType\n  name\n  __typename\n}\n\nfragment SorterFields on SorterOption {\n  type: name\n  captionTranslationTag {\n    translation\n    __typename\n  }\n  tooltipTranslationTag {\n    translation\n    __typename\n  }\n  isSelected: selected\n  __typename\n}\n\nfragment OneOfThreeDeal on OneOfThreeDeal {\n  id\n  uuid\n  winnerHotelId\n  winnerBlockId\n  priceDisplayInfo {\n    displayPrice {\n      amountPerStay {\n        amountRounded\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  locationInfo {\n    name\n    inName\n    destType\n    __typename\n  }\n  destinationType\n  commonFacilities {\n    id\n    name\n    __typename\n  }\n  properties {\n    priceDisplayInfo {\n      priceBeforeDiscount {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      displayPrice {\n        amountPerStay {\n          amountRounded\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    basicPropertyData {\n      id\n      name\n      pageName\n      photos {\n        main {\n          highResUrl {\n            absoluteUrl\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      location {\n        address\n        countryCode\n        __typename\n      }\n      reviews {\n        reviewsCount\n        totalScore\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment TripTypesData on TripTypes {\n  beach {\n    isBeachUfi\n    isEnabledBeachUfi\n    isCoastalBeachRegion\n    isBeachDestinationWithoutBeach\n    __typename\n  }\n  ski {\n    isSkiExperience\n    isSkiScaleUfi\n    __typename\n  }\n  skiResorts {\n    name\n    resortId\n    localizedTrailDistance\n    photoUrl\n    __typename\n  }\n  carouselBeach {\n    name\n    beachId\n    photoUrl\n    reviewScore\n    reviewScoreFormatted\n    translatedBeachActivities\n    translatedSandType\n    __typename\n  }\n  highestTrafficSkiRegionOfMultiRegionLowAVUfi {\n    regionId\n    regionName\n    photoUrl\n    skiRegionUfiData {\n      cityName\n      __typename\n    }\n    __typename\n  }\n  skiLandmarkData {\n    resortId\n    slopeTotalLengthFormatted\n    totalLiftsCount\n    __typename\n  }\n  __typename\n}\n\nfragment ZeroResultsSection on ZeroResultsSection {\n  title {\n    text\n    __typename\n  }\n  primaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      __typename\n    }\n    __typename\n  }\n  secondaryAction {\n    text {\n      text\n      __typename\n    }\n    action {\n      name\n      __typename\n    }\n    __typename\n  }\n  paragraphs {\n    text\n    __typename\n  }\n  type\n  __typename\n}\n\nfragment geniusVipEnrolledProgramFragment on GeniusVipEnrolledProgram {\n  metadata {\n    programType\n    __typename\n  }\n  geniusVipUIs {\n    searchResultModal {\n      title {\n        text\n        __typename\n      }\n      subtitle {\n        text\n        __typename\n      }\n      modalCategory\n      asset {\n        __typename\n        ... on Image {\n          url\n          __typename\n        }\n      }\n      cta {\n        text\n        actionString\n        actionDismiss\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
        }

        response = requests.post(
            "https://www.booking.com/dml/graphql",
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        page_names.append(
            response.json()["data"]["searchQueries"]["search"]["results"][0][
                "basicPropertyData"
            ]["pageName"]
        )

data = []
for name in page_names:
    hotel_url = f"https://www.booking.com/hotel/cz/{name}.en-gb.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaLUBiAEBmAEJuAEZyAEM2AEB6AEB-AEMiAIBqAIDuALRhYCiBsACAdICJDFmODVmMjU0LWY0ZTAtNDQ5OS1iNDFhLTFkOTBkOGEzN2I3OdgCBuACAQ&sid=17bbe3350ba8fd3998e8883df7bb3fdc&all_sr_blocks=242431901_335575801_2_2_0;checkin=2023-06-25;checkout=2023-06-30;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=242431901_335575801_2_2_0;hpos=1;matching_block_id=242431901_335575801_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=distance_from_search;sr_pri_blocks=242431901_335575801_2_2_0__31170;srepoch=1681916841;srpvid=d4b26a53c8ec0086;type=total;ucfs=1&#hotelTmpl"

    hotel_page = requests.get(hotel_url, headers=headers)
    soup = BeautifulSoup(hotel_page.text, "html.parser")

    star_rating = len(soup.select("span[data-testid=rating-stars] > span"))
    address = soup.select_one("span.hp_address_subtitle").text.strip()
    rooms = soup.select("a.hprt-roomtype-link")
    empty_rooms = soup.select(
        "tr.js-rt-block-row.e2e-hprt-table-row.hprt-table-last-row"
    )
    roomTypes = [room.text.strip() for room in rooms]
    availableRooms = [len(room.select("option")) - 1 for room in empty_rooms]
    for idx, r in enumerate(roomTypes):
        data.append(
            {
                "Hotel_Name": name,
                "Star_Rating": star_rating,
                "Address": address,
                roomTypes[idx]: availableRooms[idx],
            }
        )
    print(data)


def get_all_keys_in_order(list_of_dicts):
    ordered_keys = []
    for dict_ in list_of_dicts:
        for key in dict_:
            if key not in ordered_keys:
                ordered_keys.append(key)
    return ordered_keys


all_fieldnames = get_all_keys_in_order(data)
with open("booking.csv", "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=all_fieldnames)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    print('Stored results to "booking.csv"')
# roomType = []
# availableRooms = []
# for room in rooms:
#    roomType.append(room.text.strip())
#
# for room in empty_rooms:
#   availableRooms.append(len(room.select('option'))-1)
