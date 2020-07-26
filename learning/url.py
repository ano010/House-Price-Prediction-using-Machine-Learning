url_all = 'https://ikman.lk/en/ads/sri-lanka/property'

url_houses_all = 'https://ikman.lk/en/ads/sri-lanka/houses?categoryType=ads'

url_houses_rent_only = 'https://ikman.lk/en/ads/sri-lanka/houses?categoryType=ads&type=for_rent'

url_land_all = 'https://ikman.lk/en/ads/sri-lanka/land?categoryType=ads'

url_land_rent_only = 'https://ikman.lk/en/ads/sri-lanka/land?categoryType=ads&type=for_rent'

url_apartments_all = 'https://ikman.lk/en/ads/sri-lanka/apartments?categoryType=ads'

url_apartments_rent_only = 'https://ikman.lk/en/ads/sri-lanka/apartments?categoryType=ads&type=for_rent'

url_commercial_property = 'https://ikman.lk/en/ads/sri-lanka/commercial-property?categoryType=ads&type=for_rent'

url_short_term = 'https://ikman.lk/en/ads/sri-lanka/holiday-short-term-rental?categoryType=ads'

url_rooms = 'https://ikman.lk/en/ads/sri-lanka/rooms-annexes?categoryType=ads'

url_newDevelopment = 'https://ikman.lk/en/ads/sri-lanka/new-developments?categoryType=ads'

propertyTypes = [
    'houses',
    'land',
    'apartments',
    'commercial-property',
    'holiday-short-term-rental',
    'new-developments'
]



def getUrl(propertyType, place):
    url = 'https://ikman.lk/en/ads/'
    url += place
    url +='/'
    url += propertyType
    return url;

districts = [
    # 'gampaha',
    'colombo',
    # # 'kalutara',
    # # 'kandy',
    # # 'kurunegala',
    # # 'ampara',
    # # 'anuradhapura',
    # # 'badulla',
    # # 'batticaloa',
    # # 'galle',
    # # 'hambantota',
    # # 'jaffna',
    # # 'kegalle',
    # # 'kilinochchi',
    # # 'mannar',
    # # 'matale',
    # # 'matara',
    # # 'moneragala',
    # # 'mullativu',
    # # 'nuwara-eliya',
    # 'polonnaruwa',
    # 'puttalam',
    # 'ratnapura',
    # 'trincomalee',
    # 'vavuniya'
]

placesDict = {
    'gampaha': [
        'negombo',
        'kadawatha',
        'wattala',
        'ja-ela',
        'delgoda',
        'divulapitiya',
        'ganemulla',
        'kandana',
        'katunayake',
        'kelaniya',
        'kiribathgoda',
        'minuwangoda',
        'mirigama',
        'nittambuwa',
        'ragama',
        'veyangoda',

    ],
    'colombo': ['colombo-6',
                'dehiwala',
                'malabe',
                'mount-lavinia',
                'nugegoda',
                'angoda',
                'athurugiriya',
                'avissawella',
                'battaramulla',
                'boralesgamuwa',
                'colombo-1',
                'colombo-10',
                'colombo-11',
                'colombo-12',
                'colombo-13',
                'colombo-14',
                'colombo-15',
                'colombo-2',
                'colombo-3',
                'colombo-4',
                'colombo-5',
                'colombo-7',
                'colombo-8',
                'colombo-9',
                'hanwella',
                'homagama',
                'kaduwela',
                'kesbewa',
                'kohuwala',
                'kolonnawa',
                'kottawa',
                'kotte',
                'padukka',
                'piliyandala',
                'talawatugoda',
                'nawala',
                'pannipitiya',
                'rajagiriya',
                'moratuwa',
                'maharagama',
                'ratmalana',
                'wellampitiya'
                ],
    'kalutara': [
        'horana',
        'panadura',
        'kalutara',
        'bandaragama',
        'ingiriya',
        'alutgama',
        'beruwala',
        'matugama',
        'wadduwa',
    ],
    'kandy': [
        'peradeniya',
        'katugastota',
        'kundasale',
        'gampola',
        'akurana',
        'ampitiya',
        'digana',
        'galagedara',
        'gelioya',
        'kadugannawa',
        'nawalapitiya',
        'pilimatalawa',
        'wattegama'
    ],
    'kurunegala': [
        'kuliyapitiya',
        'pannala',
        'narammala',
        'alawwa',
        'bingiriya',
        'galgamuwa',
        'giriulla',
        'hettipola',
        'ibbagamuwa',
        'mawathagama',
        'nikaweratiya',
        'polgahawela',
        'wariyapola',
    ],
    'ampara': [
        'akkarepattu',
        'sainthamaruthu',
        'kalmunai'
    ],
    'anuradhapura': [
        'kekirawa',
        'tambuttegama',
        'medawachchiya',
        'habarana',
        'eppawala',
        'galenbindunuwewa',
        'mihintale',
        'nochchiyagama',
        'talawa'
    ],
    'badulla': [
        'badulla',
        'bandarawela',
        'welimada',
        'ella',
        'haputale',
        'diyatalawa',
        'hali-ela',
        'mahiyanganaya',
        'passara'
    ],
    'batticaloa': [],
    'galle': [
        'ambalangoda',
        'hikkaduwa',
        'elpitiya',
        'karapitiya',
        'ahangama',
        'baddegama',
        'batapola',
        'bentota'
    ],
    'hambantota': [
        'tangalla',
        'ambalantota',
        'tissamaharama',
        'beliatta'
    ],
    'jaffna': [
        'nallur',
        'chavakachcheri'
    ],
    'kegalle': [
        'mawanella',
        'rambukkana',
        'ruwanwella',
        'warakapola',
        'dehiowita',
        'deraniyagala',
        'galigamuwa',
        'kitulgala',
        'yatiyantota',
    ],
    'kilinochchi': [

    ],
    'mannar': [

    ],
    'matale': [
        'matale',
        'dambulla',
        'sigiriya',
        'ukuwela',
        'galewela',
        'palapathwela',
        'rattota',
        'yatawatta'
    ],
    'matara': [
        'weligama',
        'dikwella',
        'kekanadurra',
        'akuressa',
        'deniyaya',
        'hakmana',
        'kamburugamuwa',
        'kamburupitiya'
    ],
    'moneragala': [
        'kataragama',
        'wellawaya',
        'moneragala',
        'buttala',
        'bibile'
    ],
    'mullativu': [],
    'nuwara-eliya': [
        'hatton',
        'ginigathena',
        'madulla'
    ],
    'polonnaruwa': [
        'hingurakgoda',
        'kaduruwela',
        'medirigiriya'
    ],
    'puttalam': [
        'chilaw',
        'wennappuwa',
        'nattandiya',
        'dankotuwa',
        'marawila'
    ],
    'ratnapura': [
        'balangoda',
        'embilipitiya',
        'eheliyagoda',
        'pelmadulla',
        'kuruwita'
    ],
    'trincomalee': [
        'kinniya'
    ],
    'vavuniya': []

}

def getFileInfo(root, propertyType, rentOrSale):
    fileUrls = {}
    for index in range(len(districts)):
        district = districts[index]    
        placesArray = placesDict[district]
        fileUrls.__setitem__(district, [root, propertyType, rentOrSale, district])
        # fileUrls.append([root, propertyType, rentOrSale, district])
        if (len(placesArray) == 0):
            continue
            
        for indexInner in range(len(placesArray)):
            # fileUrls.append([root, propertyType, rentOrSale, district, placesArray[indexInner]])
            fileUrls.__setitem__(placesArray[indexInner], [root, propertyType, rentOrSale, district, placesArray[indexInner]])
    return fileUrls
