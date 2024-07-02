var createCounter = function(init) {
    var x = init;
    return {
        increment: function(){
            return ++x
        },
        reset: function(){
            x = init;
            return x
        },
        decrement: function(){
            return --x
        }
    };
};