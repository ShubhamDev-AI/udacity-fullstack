let LEVELS = [
    'Newborn',
    'Infant',
    'Preteen',
    'Teen',
    'Adult',
    'Parent',
    'Grandparent'
];

let CAT_DATA = [
    {
        name: 'Fancy Cat',
        clickCount: 0,
        imgSrc: 'img/22252709_010df3379e_z.jpg',
        imgAttribution: 'Flicker',
        nicknames: ['Tabby','Snowball','Bennyhayny']
    },
    {
        name: 'Brainy Cat',
        clickCount: 0,
        imgSrc: 'img/434164568_fea0ad4013_z.jpg',
        imgAttribution: 'Flicker',
        nicknames: ['Bella','Tigger']
    },
    {
        name: 'Brauny Cat',
        clickCount: 0,
        imgSrc: 'img/1413379559_412a540d29_z.jpg',
        imgAttribution: 'Flicker',
        nicknames: ['Chloe','Shadow','Oreo']
    },
    {
        name: 'Artsy Cat',
        clickCount: 0,
        imgSrc: 'img/4154543904_6e2428c421_z.jpg',
        imgAttribution: 'Flicker',
        nicknames: ['Lucy','Smokey','Jasper']
    },
    {
        name: 'Lazy Cat',
        clickCount: 0,
        imgSrc: 'img/9648464288_2516b35537_z.jpg',
        imgAttribution: 'Flicker',
        nicknames: ['Gizmo','Simba','Charlie']
    }
];

let CatViewModel = function(data){

    this.name = ko.observable(data.name);
    this.clickCount = ko.observable(data.clickCount);
    this.imgSrc = ko.observable(data.imgSrc);
    this.imgAttribution = ko.observable(data.imgAttribution);

    this.nicknames = ko.observableArray(data.nicknames);

    this.level = ko.computed(function(){
        let l = Math.floor(this.clickCount() / 100 * LEVELS.length);
        return LEVELS[l];
    }, this);

    this.incrementCounter = function() {
        this.clickCount(this.clickCount() + 1);
        return false;
    };
};

let AppViewModel = function(){

    this.catList = ko.observableArray([]);

    CAT_DATA.forEach(data => {
        this.catList.push(new CatViewModel(data));
    });

    this.currentCat = ko.observable(this.catList()[0]);

    this.select = (cat) => {
        this.currentCat(cat);
        return false;
    };

};


ko.applyBindings(new AppViewModel());