/**
 * TAG: #2620
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let current = n;

    return function() {
    const value = current;
        current++;
        return value;   
    };
};


/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */
