let LEVELS = [
    'Newborn',
    'Infant',
    'Preteen',
    'Teen',
    'Adult',
    'Parent',
    'Grandparent'
];

let CatViewModel = function(){

    this.name = ko.observable('Fancy Cat');
    this.clickCount = ko.observable(0);
    this.imgSrc = ko.observable('img/22252709_010df3379e_z.jpg');
    this.imgAttribution = ko.observable('Flicker');

    this.nicknames = ko.observableArray([
        'Tabby',
        'Snowball',
        'Bennyhayny'
    ]);

    this.level = ko.computed(function(){
        let l = Math.floor(this.clickCount() / 100 * LEVELS.length);
        return LEVELS[l];
    }, this);
};

let AppViewModel = function(){
    this.currentCat = ko.observable(new CatViewModel());
    this.incrementCounter = function() {
        this.currentCat().clickCount(this.currentCat().clickCount() + 1);
    };
};


ko.applyBindings(new AppViewModel());