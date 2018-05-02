

function View(){
    let appRoot = document.getElementById('app');
    let container = document.createElement('div');
    container.className = 'cat';

    this.render = function(cats){

    };
}


function Model(){
    this.cats = [];

    this.increment = function(id){
        let cat = this.cats.find((cat) => cat.id === id);
        cat.counter++;
    };

    this.add = function(name, image){
        this.cats.push({
            name: name,
            counter: 0,
            image: image,
            id: Math.floor(Math.random() * 999999)
        });
    };

    this.all = function(){
        return this.cats;
    };

}


function Controller(view, model){

}


let view = new View();
let model = new Model();
let container = new Controller(view, model);