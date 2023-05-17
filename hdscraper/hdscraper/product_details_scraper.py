
"""
This file is used to make an API request for the Home Depot website. The API request is used to get the product information for each product on the website.
"""

from pprint import pprint

import requests


def get_headers():
    """Return the headers for the API request"""
    return {
        "authority": "www.homedepot.com",
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "apollographql-client-name": "general-merchandise",
        "apollographql-client-version": "0.0.0",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "cookie": 'THD_CACHE_NAV_PERSIST=; thda.u=d4536a0c-9322-15aa-995b-026b793a80c3; _pxvid=a2e9bbaa-8bb3-11ec-9bc4-486647775261; _px_f394gi7Fvmc43dfg_user_id=YTZhMmIyOTAtOGJiMy0xMWVjLWIzMTItOWYxZTIwYmExMTY4; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2283f713c0-f03c-4f5e-bfe5-0f2e93e705fc%22; _meta_bing_beaconFired=true; _meta_facebookPixel_beaconFired=true; _meta_neustar_mcvisid=80722401008641566833652823383313760634; _meta_googleFloodlight_beaconFired=true; _gcl_au=1.1.1538251435.1644636427; trx=4940941397884565684; _meta_revjet_revjet_vid=4940941397884565684; aam_mobile=seg%3D1131078; aam_uuid=80977617910093768943663171872454602511; _ga=GA1.2.1242876952.1644636428; _meta_adobe_aam_uuid=80977617910093768943663171872454602511; _meta_neustar_aam=80977617910093768943663171872454602511; QuantumMetricUserID=2aed79d0b4169f2d96f7982f95c84d49; LPVID=k3MzIxMWZlMGRiZTI5MThk; QSI_SI_2lVW226zFt4dVJ3_intercept=true; mdLogger=false; kampyle_userid=bffc-fd39-0420-bba1-3203-33c5-b962-cfac; kampyleUserSession=1646024693073; kampyleUserSessionsCount=1; cd_user_id=17f3eb7959d7f3-05bad645ac66de-a3e3164-1fa400-17f3eb7959e809; WORKFLOW=LOCALIZED_BY_GPS_HIGH; DELIVERY_ZIP_TYPE=AUTO; THD_PERSIST=C4%3D620%2BHawthorne%20-%20Hawthorne%2C%20CA%2B%3A%3BC4_EXP%3D1677617852%3A%3BC24%3D90250%3A%3BC24_EXP%3D1677617852%3A%3BC39%3D1%3B7%3A00-20%3A00%3B2%3B6%3A00-22%3A00%3B3%3B6%3A00-22%3A00%3B4%3B6%3A00-22%3A00%3B5%3B6%3A00-22%3A00%3B6%3B6%3A00-22%3A00%3B7%3B6%3A00-22%3A00%3A%3BC39_EXP%3D1646117287; ffvisitorids={"homedepot_flooring":"adc65a8a4a1340128cc1c85b14a504ec"}; ffvendorids={"homedepot_flooring":"9b6c15f595f74d568f5dbaa2f1b046f8"}; _meta_roomvo_ffvisitorids={"homedepot_flooring":"adc65a8a4a1340128cc1c85b14a504ec"}; DELIVERY_ZIP=40207; _meta_metarouter_timezone_offset=420; _meta_google_ga=1242876952.1644636428; _meta_google_cookie_ga=GA1.2.1242876952.1644636428; _meta_xandr_uid=7239243502407885188; _meta_xandr_uid2=uuid2=7239243502407885188; _meta_amobee_uid=3474695812977077561; _meta_yahooMedia_yahoo_id=y-_QDC9T5E2r2UxwZlUl3A3k7dVYi3YUj_eCYD~A; _meta_mediaMath_mm_id=d75661a0-949b-4400-ba70-7c1cb5c3560a; _meta_mediaMath_cid=d75661a0-949b-4400-ba70-7c1cb5c3560a; _meta_google_cookie_gid=GA1.2.1039004236.1648098456; mp_0e3ea14e7e90fc91592bf29cb9917ec6_mixpanel=%7B%22distinct_id%22%3A%20%2217f3eb78f2e204-0ecf960ace616c-a3e3164-1fa400-17f3eb78f2f711%22%2C%22%24device_id%22%3A%20%2217f3eb78f2e204-0ecf960ace616c-a3e3164-1fa400-17f3eb78f2f711%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.homedepot.com%2Fc%2Fsite_map%22%2C%22%24initial_referring_domain%22%3A%20%22www.homedepot.com%22%7D; LOCALIZED_STORE_INFO={%22zipcode%22:%2240207%22%2C%22storeId%22:%222313%22%2C%22state%22:%22KY%22%2C%22name%22:%22St%20Matthews%22%2C%22city%22:%22Louisville%22}; kampyleSessionPageCounter=2; invoca_session=%7B%22ttl%22%3A%222022-03-29T00%3A13%3A28.951Z%22%2C%22session%22%3A%7B%22invoca_id%22%3A%22i-198065b4-ea3a-4458-b55b-11e18f234027%22%7D%2C%22config%22%3A%7B%22ce%22%3Atrue%2C%22fv%22%3Afalse%2C%22rn%22%3Afalse%7D%7D; HD_DC=beta; akacd_usbeta=3827073484~rv=5~id=133964885f66cb44dec2cec53263710b; at_check=true; AMCVS_F6421253512D2C100A490D45%40AdobeOrg=1; THD_SESSION=; THD_CACHE_NAV_SESSION=; thda.s=c326921d-7232-de1e-bbd3-c1bad1a3dd87; _meta_movableInk_mi_u=83f713c0-f03c-4f5e-bfe5-0f2e93e705fc; thda.m=80722401008641566833652823383313760634; _meta_pinterest_derived_epik_failure=true; _gid=GA1.2.525700664.1649620693; _meta_acuityAds_auid=625401118457; _meta_acuityAds_cauid=auid=625401118457; AMCV_F6421253512D2C100A490D45%40AdobeOrg=1585540135%7CMCIDTS%7C19093%7CMCMID%7C80722401008641566833652823383313760634%7CMCAAMLH-1650255029%7C9%7CMCAAMB-1650255029%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1649657430s%7CNONE%7CMCCIDH%7C1740013322%7CvVersion%7C4.4.0; ecrSessionId=D871DDE78A97D9937F1AD38BBA1F007B; forterToken=88668bf20f7b4c939142d40ce81a9b8d_1649656212215__UDF43_13ck; _meta_mediaMath_iframe_counter=5; LPSID-31564604=wXhDsfi6TZGsgB3t8TzkRg; _px=NaxQAg4iUI97rdMFHa38qiALu+Np8EgA4Axi4HFWA2tkK1O+AvPa6baboKSS4znKAcA6aH2ahJaxmyF+pZC9WQ==:1000:toSazmYFqLN6QjqEvB9WYVwnv/UizGdXA5F5Umu/+tDfTV39nK8FS4xFmgoqbcrZEKYSiprzbsTHtKbmTcO+nDEv1Q35QUKca3CwKZQH0LAt304oTVsM3nc9R9yScX7qw2aTcm/FAW4zSLxbCxXgWezgMnaYnv9kGLhDfKD2dFj4vC9fs+PN/cC2etYEotW2KSWeQazlf4lXgBFhluYJIZ7oaKxLcPGeKFaxJoguM/8KDty4wjyNBbyGs4+TGxFiE33hkSvxAgbw68xNP7Tnvw==; _pxde=0af3277719f4a22a151b125ab5da5c26724bad163812ff206cac453d46ba954d:eyJ0aW1lc3RhbXAiOjE2NDk2NjQ2MTgwNTV9; QuantumMetricSessionID=f7b9ca16bc1be019a761ddd796b7e5a3; _abck=588AD3A2D6450BE424C494AE57686AE7~0~YAAQ2KXcFwOtpwGAAQAAVPZPGQf/yFkoK19l1t2Z1o9W2VYUP4UVhY63msx5rNGk83nv5l7WuLrdrkkIryWbZ+q/WqBMGjX2scP40MDy5cyyBygG8kFoEoO9doJ25W5VR7V5EaTJ+hjHZEoWMDFLZJo0kWBODeAQMnWnQQ9R+Z+Mv9LJUHcJoWP3KY4z+dbJRXQR9urZA0ZsSSm54MaGpfTvUL9RguLIubD/yEm4vE7GjC0BaYPlu3xNFuqlr9hlF65SSZF+OXcoYi8F3YQIvemmtF2nPhfO+NSa2l+BVB/z9dAUlY3DDjgD57Qhdfst4w5d0Uc22G42IsS1GuIpeL/xQItpXb7rilPNOCNxzLLqsmsup9KNy88l4eyuPnhU1TtBXx96Qf7ipXt338qbPru0E3Zat/e3IqYz~-1~-1~-1; bm_sz=CF813751BE3D5E380AE7F27309A0C5B9~YAAQ2KXcFwWtpwGAAQAAVPZPGQ80dImExdagV6ce8era0KjRDaytVkFWMkvOLJk624/6HFOGG6iq2masJup9Bckmk0Y6Rid/Yw35rl4UHR7CoNRg/xIJNRYba303H8t27ziV7C9AXYhXe07J3UQeDNfd+yLpQfPkANeVq/3C5SjpSZa5g/9dOlOTivoOk9XUqpJ7xVW/E2UrEo0ojTctHLgsE/USxHTKpg5G2mH+TSZl0iEueHsqSmx6OZyIjwYvJQvzLlqvO4q2zI7diIGge+Dojmhcz0xvf+MEjqdGgG7ieK/eWv4=~3490353~3616838; s_pers=%20productnum%3D15%7C1651018406409%3B%20s_nr365%3D1649693758390-Repeat%7C1681229758390%3B%20s_dslv%3D1649693758404%7C1744301758404%3B; s_sq=%5B%5BB%5D%5D; _gat=1; s_sess=%20s_cc%3Dtrue%3B%20s_pv_pName%3Dappliances%253Evacuum%2520cleaners%253Epagination%3B%20s_pv_pType%3Dcat%2520plp%3B%20s_pv_cmpgn%3D%3B%20s_pv_pVer%3Dplp%253Aversion%253Agen2%3B%20stsh%3D%3B; QSI_HistorySession=https%3A%2F%2Fwww.homedepot.com%2Fb%2FAppliances-Vacuum-Cleaners%2FN-5yc1vZbv74%3F%26catStyle%3DShowProducts%26Nao%3D24~1649620692232%7Chttps%3A%2F%2Fwww.homedepot.com%2Fc%2Fsite_map~1649622481719%7Chttps%3A%2F%2Fwww.homedepot.com%2Fb%2FAppliances-Vacuum-Cleaners%2FN-5yc1vZbv74~1649622511219%7Chttps%3A%2F%2Fwww.homedepot.com%2Fb%2FAppliances-Vacuum-Cleaners%2FN-5yc1vZbv74%3FNao%3D24~1649693759784; AKA_A2=A; THD_NR=1; bm_mi=D16E83AB1D92EEC4BC10ED0ED4646E87~h/fxaiFcsCeOIuRXLtM7iQYbeo67IHjI7HXEmgghGmS8DbXmrIamBtNXfK1czF3fBfgtkaz3v1nxHf0XnQsecQA3LCaQHTdUqUvIESBvJND9wvwLRkXXDoD0Ik8Q6FT22e71T2W4Laj7W9an/BrX2o/vKJ2LuLOKWSyKjrdUf9VPIWrccRbItH3gvlF9+iD/HJznOvHbzGUlkqkfiMZZDc78oIuQoIULeM0r/fCUWcqgUGMeWE8vz8K2Ux13ZZlSfvR3MZQSNxSpnNKILD41yR7Rybp6OgK4ReJFI6BAjUukIfEVdfxEkVY7EjISz+wgKSIo8mzMXl0REWkosioYZA==; mbox=PC#5e2417bbed024e7d81b230c38c088323.35_0#1712938564|session#3dd6f4dbb48045b281f6afed9aa5ad27#1649695624; IN_STORE_API_SESSION=TRUE; RT="z=1&dm=www.homedepot.com&si=3db19973-3b33-4724-9a5e-319157233e49&ss=l1uaphz3&sl=0&tt=0&bcn=%2F%2F17de4c17.akstat.io%2F"; ak_bmsc=450C242EC1FF3D6B7B57746DC676A37E~000000000000000000000000000000~YAAQpyMduBa3/hiAAQAAnzhpGQ+S2/7G/QYsalE1azk/02mG+/zArUGxN3RYEFn4IOjwghxCSLKNQwp5EoWq7OQKkGku+9RI+nOieOdjCmtXz3kyop0CPbxhpNKaGADWEyEiYTybI0Mi4i116fVTmFvn/k4JRuSAna7nsb/JUAhjuSgaU9Pj0J+3NCAgloKyAFMopsb34sFXKKG2TibpmCGOSxGSOk+4e1cW9SATG34qvKC2e0zC14eAo7Yf5IhmXXTfStvH7TKYXKlgVot+ZfwNK/gxlcJWAppZbmnqE2XbUuKeiREGMoLEL2Qt0JWZ/8hQb83k7d2n5BpIP71b6lr6G2O+uApIhqw9qOYZv2i3vNPGD2rnP5ym4xWj8GOD71HngBiTbNSFrmuNXCzMqYzvyFOYdxg91oo=; THD_LOCALIZER=%257B%2522WORKFLOW%2522%253A%2522LOCALIZED_BY_STORE%2522%252C%2522THD_FORCE_LOC%2522%253A%25220%2522%252C%2522THD_INTERNAL%2522%253A%25220%2522%252C%2522THD_LOCSTORE%2522%253A%25222313%252BSt%2520Matthews%2520-%2520Louisville%252C%2520KY%252B%2522%252C%2522THD_STRFINDERZIP%2522%253A%252240207%2522%252C%2522THD_STORE_HOURS%2522%253A%25221%253B8%253A00-18%253A00%253B2%253B6%253A00-22%253A00%253B3%253B6%253A00-22%253A00%253B4%253B6%253A00-22%253A00%253B5%253B6%253A00-22%253A00%253B6%253B6%253A00-22%253A00%253B7%253B6%253A00-22%253A00%2522%252C%2522THD_STORE_HOURS_EXPIRY%2522%253A1649697367%257D; HD_DC=beta; _abck=588AD3A2D6450BE424C494AE57686AE7~-1~YAAQtxoyuNetyQCAAQAAJ/17GQdZ00G3Hkazm4qEIn78US6LkxmcjYSoSyASLwbMxaMTTUulnCReXlg/lZN3ZJrtgKVxNjeQMkCFezjg1nWTc5usQqr5AdnRPNYzgMkNP9x8Hw/7CMuxaHCMn5AwmLpsO2tCcV0wy9hKt771ZU6NjYjLP+eEu0DK05re4QxcQlpWyoGXwtiK71idg+4omOWDvowBHKEDrFupWzY5fJq4xXYbpGiK+Xflx3ik7QNGdywrzi89xj9KXbfZYVYjjJIk5yOLhux5sCaD6MqI+vvf+kXqf1WkWKIDwkcyyfRbjKlb7PAnJNFyNrYlDbrmHcTm0jhqke2G8fUCoEHNimLtIrlTkc2feFAg9MTs4J1+6BNMF1NgA+gSBtZLuTPkw0toXzjlXyBqhyQd~0~-1~-1; ak_bmsc=450C242EC1FF3D6B7B57746DC676A37E~000000000000000000000000000000~YAAQtxoyuNityQCAAQAAJ/17GQ9CK7WfrQU2e2PaVgnFWZWTaQUmHBxxqNZoNITVD+gexKGCho4YW+0y9+97/gll+Zx1PHOL0RUFKLVZrX3zvFreDusq9mxjIPZDB6F+CQD18iyjeVbZqoBxxVid8I3QSppkyrj4rNoJCD8MWEZEh5S+5dQdUVEryTSzR6Y1qKGDVkr9ps3/GpBVc61lM+Lri5lYXHrujcrdC6ZDCMGRPqwOpcK1PIyNsdkHEgOE/Op8pFdrAKBH710Oa0Wrx1yoGnCGFjAd0QtSmbqyJhLJJJodtW/tXUDIe5ZHKeRPdgLKBjXrFK5J1E3ESbsffHrWBzwqshnnOmVLqwWFUrqPYSRuatEw6IUBsRL+xbypZN0p4Y5CCrsZWA8iWGVUhSEnTsBtdbR61wjIQIynCfkhho5waEiJkaEhXaWZ/spXOeU0bF+rvd4RCgu18Y1lg3GARxO2nQhqXg==',
        "dnt": "1",
        "origin": "https://www.homedepot.com",
        "pragma": "no-cache",
        "referer": "https://www.homedepot.com/c/site_map",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36",
        "x-api-cookies": '{"x-user-id":"d4536a0c-9322-15aa-995b-026b793a80c3"}',
        "x-current-url": "c/site_map",
        "x-debug": "false",
        "x-experience-name": "general-merchandise",
        "x-hd-dc": "beta",
    }

def create_payload(updated_index, code):
    """Create the JSON payload for the API request"""
    return {
        "operationName": "searchModel",
        "variables": {
            "skipInstallServices": False,
            "skipKPF": False,
            "skipSpecificationGroup": False,
            "skipSubscribeAndSave": False,
            "storefilter": "ALL",
            "channel": "DESKTOP",
            "additionalSearchParams": {
                "sponsored": True,
                "mcvisId": "80722401008641566833652823383313760634",
                "deliveryZip": "90254",
            },
            "filter": {},
            "navParam": code,
            "orderBy": {"field": "TOP_SELLERS", "order": "ASC"},
            "pageSize": 24,
            "startIndex": updated_index,
            "storeId": "0620",
        },
        "query": "query searchModel($storeId: String, $zipCode: String, $skipInstallServices: Boolean = true, $startIndex: Int, $pageSize: Int, $orderBy: ProductSort, $filter: ProductFilter, $skipKPF: Boolean = false, $skipSpecificationGroup: Boolean = false, $skipSubscribeAndSave: Boolean = false, $keyword: String, $navParam: String, $storefilter: StoreFilter = ALL, $itemIds: [String], $channel: Channel = DESKTOP, $additionalSearchParams: AdditionalParams, $loyaltyMembershipInput: LoyaltyMembershipInput) {\n  searchModel(keyword: $keyword, navParam: $navParam, storefilter: $storefilter, storeId: $storeId, itemIds: $itemIds, channel: $channel, additionalSearchParams: $additionalSearchParams, loyaltyMembershipInput: $loyaltyMembershipInput) {\n    metadata {\n      hasPLPBanner\n      categoryID\n      analytics {\n        semanticTokens\n        dynamicLCA\n        __typename\n      }\n      canonicalUrl\n      searchRedirect\n      clearAllRefinementsURL\n      contentType\n      isStoreDisplay\n      productCount {\n        inStore\n        __typename\n      }\n      stores {\n        storeId\n        storeName\n        address {\n          postalCode\n          __typename\n        }\n        nearByStores {\n          storeId\n          storeName\n          distance\n          address {\n            postalCode\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    products(startIndex: $startIndex, pageSize: $pageSize, orderBy: $orderBy, filter: $filter) {\n      identifiers {\n        storeSkuNumber\n        canonicalUrl\n        brandName\n        itemId\n        productLabel\n        modelNumber\n        productType\n        parentId\n        isSuperSku\n        __typename\n      }\n      installServices(storeId: $storeId, zipCode: $zipCode) @skip(if: $skipInstallServices) {\n        scheduleAMeasure\n        gccCarpetDesignAndOrderEligible\n        __typename\n      }\n      itemId\n      dataSources\n      media {\n        images {\n          url\n          type\n          subType\n          sizes\n          __typename\n        }\n        __typename\n      }\n      pricing(storeId: $storeId) {\n        value\n        alternatePriceDisplay\n        alternate {\n          bulk {\n            pricePerUnit\n            thresholdQuantity\n            value\n            __typename\n          }\n          unit {\n            caseUnitOfMeasure\n            unitsOriginalPrice\n            unitsPerCase\n            value\n            __typename\n          }\n          __typename\n        }\n        original\n        mapAboveOriginalPrice\n        message\n        preferredPriceFlag\n        promotion {\n          type\n          description {\n            shortDesc\n            longDesc\n            __typename\n          }\n          dollarOff\n          percentageOff\n          savingsCenter\n          savingsCenterPromos\n          specialBuySavings\n          specialBuyDollarOff\n          specialBuyPercentageOff\n          dates {\n            start\n            end\n            __typename\n          }\n          __typename\n        }\n        specialBuy\n        unitOfMeasure\n        __typename\n      }\n      reviews {\n        ratingsReviews {\n          averageRating\n          totalReviews\n          __typename\n        }\n        __typename\n      }\n      availabilityType {\n        discontinued\n        type\n        __typename\n      }\n      badges(storeId: $storeId) {\n        name\n        __typename\n      }\n      details {\n        collection {\n          collectionId\n          name\n          url\n          __typename\n        }\n        __typename\n      }\n      favoriteDetail {\n        count\n        __typename\n      }\n      fulfillment(storeId: $storeId, zipCode: $zipCode) {\n        backordered\n        backorderedShipDate\n        bossExcludedShipStates\n        excludedShipStates\n        seasonStatusEligible\n        fulfillmentOptions {\n          type\n          fulfillable\n          services {\n            type\n            hasFreeShipping\n            freeDeliveryThreshold\n            locations {\n              curbsidePickupFlag\n              isBuyInStoreCheckNearBy\n              distance\n              inventory {\n                isOutOfStock\n                isInStock\n                isLimitedQuantity\n                isUnavailable\n                quantity\n                maxAllowedBopisQty\n                minAllowedBopisQty\n                __typename\n              }\n              isAnchor\n              locationId\n              storeName\n              state\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      info {\n        hasSubscription\n        isBuryProduct\n        isSponsored\n        isGenericProduct\n        isLiveGoodsProduct\n        sponsoredBeacon {\n          onClickBeacon\n          onViewBeacon\n          __typename\n        }\n        sponsoredMetadata {\n          campaignId\n          placementId\n          slotId\n          __typename\n        }\n        globalCustomConfigurator {\n          customExperience\n          __typename\n        }\n        returnable\n        hidePrice\n        productSubType {\n          name\n          link\n          __typename\n        }\n        categoryHierarchy\n        samplesAvailable\n        customerSignal {\n          previouslyPurchased\n          __typename\n        }\n        productDepartmentId\n        productDepartment\n        augmentedReality\n        ecoRebate\n        quantityLimit\n        sskMin\n        sskMax\n        unitOfMeasureCoverage\n        wasMaxPriceRange\n        wasMinPriceRange\n        swatches {\n          isSelected\n          itemId\n          label\n          swatchImgUrl\n          url\n          value\n          __typename\n        }\n        totalNumberOfOptions\n        paintBrand\n        dotComColorEligible\n        __typename\n      }\n      keyProductFeatures @skip(if: $skipKPF) {\n        keyProductFeaturesItems {\n          features {\n            name\n            refinementId\n            refinementUrl\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      specificationGroup @skip(if: $skipSpecificationGroup) {\n        specifications {\n          specName\n          specValue\n          __typename\n        }\n        specTitle\n        __typename\n      }\n      subscription @skip(if: $skipSubscribeAndSave) {\n        defaultfrequency\n        discountPercentage\n        subscriptionEnabled\n        __typename\n      }\n      sizeAndFitDetail {\n        attributeGroups {\n          attributes {\n            attributeName\n            dimensions\n            __typename\n          }\n          dimensionLabel\n          productType\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    id\n    searchReport {\n      totalProducts\n      didYouMean\n      correctedKeyword\n      keyword\n      pageSize\n      searchUrl\n      sortBy\n      sortOrder\n      startIndex\n      __typename\n    }\n    relatedResults {\n      universalSearch {\n        title\n        __typename\n      }\n      relatedServices {\n        label\n        __typename\n      }\n      visualNavs {\n        label\n        imageId\n        webUrl\n        categoryId\n        imageURL\n        __typename\n      }\n      visualNavContainsEvents\n      relatedKeywords {\n        keyword\n        __typename\n      }\n      __typename\n    }\n    taxonomy {\n      brandLinkUrl\n      breadCrumbs {\n        browseUrl\n        creativeIconUrl\n        deselectUrl\n        dimensionId\n        dimensionName\n        label\n        refinementKey\n        url\n        __typename\n      }\n      __typename\n    }\n    templates\n    partialTemplates\n    dimensions {\n      label\n      refinements {\n        refinementKey\n        label\n        recordCount\n        selected\n        imgUrl\n        url\n        nestedRefinements {\n          label\n          url\n          recordCount\n          refinementKey\n          __typename\n        }\n        __typename\n      }\n      collapse\n      dimensionId\n      isVisualNav\n      isVisualDimension\n      nestedRefinementsLimit\n      visualNavSequence\n      __typename\n    }\n    orangeGraph {\n      universalSearchArray {\n        pods {\n          title\n          description\n          imageUrl\n          link\n          recordType\n          __typename\n        }\n        info {\n          title\n          __typename\n        }\n        __typename\n      }\n      productTypes\n      intents\n      orderNumber\n      __typename\n    }\n    appliedDimensions {\n      label\n      refinements {\n        label\n        refinementKey\n        url\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
    }

def make_api_request(url, headers, payload):
    """Make API request and return the response"""
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        print(f"Error making API request: {exc}")
        return None


def extract_product_data(product):
    """Extract relevant data from a product"""
    info = product.get("info", {})
    identifiers = product.get("identifiers", {})
    pricing = product.get("pricing", {})
    
    return {
        "category": info.get("categoryHierarchy"),
        "brand_name": identifiers.get("brandName"),
        "item_id": identifiers.get("itemId"),
        "model_number": identifiers.get("modelNumber"),
        "product_description": identifiers.get("productLabel"),
        "price": pricing.get("value"),
        "product_url": f"https://www.homedepot.com/{identifiers.get('canonicalUrl')}"
    }


def process_products(products):
    """Process and print information about the products"""
    for product in products:
        data = extract_product_data(product)
        pprint(data)
        print("------------------------")
    print(len(products), "products processed")


def get_product_data(code, size):
    """Retrieve and process product data for a given category"""
    search_url = "https://www.homedepot.com/federation-gateway/graphql?opname=searchModel"
    index = 0
    total_products = None
    headers = get_headers()

    while total_products is None or index < total_products:
        payload = create_payload(index, code)
        response = make_api_request(search_url, headers, payload)

        if response:
            data = response.get("data", {})
            search_model = data.get("searchModel", {})
            products = search_model.get("products", [])
            search_report = search_model.get("searchReport", {})

            total_products = search_report.get("totalProducts")

            process_products(products)
            index += size


# pylint: disable=C0103
category_code = "5yc1vZbmgp"  # Replace with the desired category code
page_size = 48  # Number of products to fetch per request

get_product_data(category_code, page_size)
