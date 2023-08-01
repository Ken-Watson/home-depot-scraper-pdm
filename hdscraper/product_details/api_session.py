"""
This file is used to make an API request for the 
Home Depot website. The API request is used to get
the product information for each product on the website.
"""

import requests


class ApiSession:
    """Class to make API requests to the Home Depot website"""
    def __init__(self, url: str):
        self.url = url
        self.session = requests.Session()

    def _get_headers(self, url: str) -> dict:
        """Return the headers for the API request"""
        return {
            "authority": "www.homedepot.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "apollographql-client-name": "general-merchandise",
            "apollographql-client-version": "0.0.0",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://www.homedepot.com",
            "pragma": "no-cache",
            "referer": url,
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

    def _create_payload(self, updated_index: int, category_code: str) -> dict:
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
                    "plp": True
                },
                "filter": {},
                "navParam": category_code,
                "orderBy": {"field": "TOP_SELLERS", "order": "ASC"},
                "pageSize": 24,
                "startIndex": updated_index,
                "storeId": "0620",
            },
            "query": "query searchModel($storeId: String, $zipCode: String, $skipInstallServices: Boolean = true, $startIndex: Int, $pageSize: Int, $orderBy: ProductSort, $filter: ProductFilter, $skipKPF: Boolean = false, $skipSpecificationGroup: Boolean = false, $skipSubscribeAndSave: Boolean = false, $keyword: String, $navParam: String, $storefilter: StoreFilter = ALL, $itemIds: [String], $channel: Channel = DESKTOP, $additionalSearchParams: AdditionalParams, $loyaltyMembershipInput: LoyaltyMembershipInput) {\n  searchModel(keyword: $keyword, navParam: $navParam, storefilter: $storefilter, storeId: $storeId, itemIds: $itemIds, channel: $channel, additionalSearchParams: $additionalSearchParams, loyaltyMembershipInput: $loyaltyMembershipInput) {\n    metadata {\n      hasPLPBanner\n      categoryID\n      analytics {\n        semanticTokens\n        dynamicLCA\n        __typename\n      }\n      canonicalUrl\n      searchRedirect\n      clearAllRefinementsURL\n      contentType\n      isStoreDisplay\n      productCount {\n        inStore\n        __typename\n      }\n      stores {\n        storeId\n        storeName\n        address {\n          postalCode\n          __typename\n        }\n        nearByStores {\n          storeId\n          storeName\n          distance\n          address {\n            postalCode\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    products(startIndex: $startIndex, pageSize: $pageSize, orderBy: $orderBy, filter: $filter) {\n      identifiers {\n        storeSkuNumber\n        canonicalUrl\n        brandName\n        itemId\n        productLabel\n        modelNumber\n        productType\n        parentId\n        isSuperSku\n        __typename\n      }\n      installServices(storeId: $storeId, zipCode: $zipCode) @skip(if: $skipInstallServices) {\n        scheduleAMeasure\n        gccCarpetDesignAndOrderEligible\n        __typename\n      }\n      itemId\n      dataSources\n      media {\n        images {\n          url\n          type\n          subType\n          sizes\n          __typename\n        }\n        __typename\n      }\n      pricing(storeId: $storeId) {\n        value\n        alternatePriceDisplay\n        alternate {\n          bulk {\n            pricePerUnit\n            thresholdQuantity\n            value\n            __typename\n          }\n          unit {\n            caseUnitOfMeasure\n            unitsOriginalPrice\n            unitsPerCase\n            value\n            __typename\n          }\n          __typename\n        }\n        original\n        mapAboveOriginalPrice\n        message\n        preferredPriceFlag\n        promotion {\n          type\n          description {\n            shortDesc\n            longDesc\n            __typename\n          }\n          dollarOff\n          percentageOff\n          savingsCenter\n          savingsCenterPromos\n          specialBuySavings\n          specialBuyDollarOff\n          specialBuyPercentageOff\n          dates {\n            start\n            end\n            __typename\n          }\n          __typename\n        }\n        specialBuy\n        unitOfMeasure\n        __typename\n      }\n      reviews {\n        ratingsReviews {\n          averageRating\n          totalReviews\n          __typename\n        }\n        __typename\n      }\n      availabilityType {\n        discontinued\n        type\n        __typename\n      }\n      badges(storeId: $storeId) {\n        name\n        __typename\n      }\n      details {\n        collection {\n          collectionId\n          name\n          url\n          __typename\n        }\n        __typename\n      }\n      favoriteDetail {\n        count\n        __typename\n      }\n      fulfillment(storeId: $storeId, zipCode: $zipCode) {\n        backordered\n        backorderedShipDate\n        bossExcludedShipStates\n        excludedShipStates\n        seasonStatusEligible\n        fulfillmentOptions {\n          type\n          fulfillable\n          services {\n            type\n            hasFreeShipping\n            freeDeliveryThreshold\n            locations {\n              curbsidePickupFlag\n              isBuyInStoreCheckNearBy\n              distance\n              inventory {\n                isOutOfStock\n                isInStock\n                isLimitedQuantity\n                isUnavailable\n                quantity\n                maxAllowedBopisQty\n                minAllowedBopisQty\n                __typename\n              }\n              isAnchor\n              locationId\n              storeName\n              state\n              type\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      info {\n        hasSubscription\n        isBuryProduct\n        isSponsored\n        isGenericProduct\n        isLiveGoodsProduct\n        sponsoredBeacon {\n          onClickBeacon\n          onViewBeacon\n          __typename\n        }\n        sponsoredMetadata {\n          campaignId\n          placementId\n          slotId\n          __typename\n        }\n        globalCustomConfigurator {\n          customExperience\n          __typename\n        }\n        returnable\n        hidePrice\n        productSubType {\n          name\n          link\n          __typename\n        }\n        categoryHierarchy\n        samplesAvailable\n        customerSignal {\n          previouslyPurchased\n          __typename\n        }\n        productDepartmentId\n        productDepartment\n        augmentedReality\n        ecoRebate\n        quantityLimit\n        sskMin\n        sskMax\n        unitOfMeasureCoverage\n        wasMaxPriceRange\n        wasMinPriceRange\n        swatches {\n          isSelected\n          itemId\n          label\n          swatchImgUrl\n          url\n          value\n          __typename\n        }\n        totalNumberOfOptions\n        paintBrand\n        dotComColorEligible\n        __typename\n      }\n      keyProductFeatures @skip(if: $skipKPF) {\n        keyProductFeaturesItems {\n          features {\n            name\n            refinementId\n            refinementUrl\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      specificationGroup @skip(if: $skipSpecificationGroup) {\n        specifications {\n          specName\n          specValue\n          __typename\n        }\n        specTitle\n        __typename\n      }\n      subscription @skip(if: $skipSubscribeAndSave) {\n        defaultfrequency\n        discountPercentage\n        subscriptionEnabled\n        __typename\n      }\n      sizeAndFitDetail {\n        attributeGroups {\n          attributes {\n            attributeName\n            dimensions\n            __typename\n          }\n          dimensionLabel\n          productType\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    id\n    searchReport {\n      totalProducts\n      didYouMean\n      correctedKeyword\n      keyword\n      pageSize\n      searchUrl\n      sortBy\n      sortOrder\n      startIndex\n      __typename\n    }\n    relatedResults {\n      universalSearch {\n        title\n        __typename\n      }\n      relatedServices {\n        label\n        __typename\n      }\n      visualNavs {\n        label\n        imageId\n        webUrl\n        categoryId\n        imageURL\n        __typename\n      }\n      visualNavContainsEvents\n      relatedKeywords {\n        keyword\n        __typename\n      }\n      __typename\n    }\n    taxonomy {\n      brandLinkUrl\n      breadCrumbs {\n        browseUrl\n        creativeIconUrl\n        deselectUrl\n        dimensionId\n        dimensionName\n        label\n        refinementKey\n        url\n        __typename\n      }\n      __typename\n    }\n    templates\n    partialTemplates\n    dimensions {\n      label\n      refinements {\n        refinementKey\n        label\n        recordCount\n        selected\n        imgUrl\n        url\n        nestedRefinements {\n          label\n          url\n          recordCount\n          refinementKey\n          __typename\n        }\n        __typename\n      }\n      collapse\n      dimensionId\n      isVisualNav\n      isVisualDimension\n      nestedRefinementsLimit\n      visualNavSequence\n      __typename\n    }\n    orangeGraph {\n      universalSearchArray {\n        pods {\n          title\n          description\n          imageUrl\n          link\n          recordType\n          __typename\n        }\n        info {\n          title\n          __typename\n        }\n        __typename\n      }\n      productTypes\n      intents\n      orderNumber\n      __typename\n    }\n    appliedDimensions {\n      label\n      refinements {\n        label\n        refinementKey\n        url\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
        }

    def make_api_request(self, api_url, index, category_code) -> dict:
        """
        Make API request and return the response. An index is
        required for the page size and offset. The category code
        is also required.
        """
        headers = self._get_headers(f"{self.url}")
        payload = self._create_payload(index, category_code)

        # Update headers for this session
        self.session.headers.update(headers)

        try:
            response = self.session.post(api_url, headers=headers, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as exc:
            print(f"Error making API request: {exc}")
            return {}
