var expect = function(val) {
   return {
        toBe: function(ob) {
            if (val === ob) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        notToBe: function(ob) {
            if (val !== ob) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
};