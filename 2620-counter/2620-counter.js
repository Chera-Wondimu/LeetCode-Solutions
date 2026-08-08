/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    return function() {
        const current = n;
        n = n +1;
        return current;
        
    };
};

