define([], function() {
    return {
        GET: function(req) {
            req.sendResponse({
                msg: "hello from GET handler",
                inputData: req.meta().queries
            });
        },

        POST: function(req) {
            print ("=============");
            print (req.data());
            print ("=============");
            req.sendResponse({
                msg: "hello from POST handler",
                inputData: req.data()
            });
        }
    };
});
