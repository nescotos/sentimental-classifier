var config = require('../config');
var zerorpc = require("zerorpc");
var client = new zerorpc.Client();
client.connect(config.MODEL_SERVER + ":" + config.MODEL_PORT);
module.exports = {
  predictSentimentSentence : function(req, res){
    client.invoke("predict_sentence", req.body.sentence , function(error, reply, streaming) {
        if(error){
            console.log("ERROR: ", error);
            res.json({success: false, message: 'Try later'});
        }else{
          res.json({success: true, results : { prediction : reply[0], positive_prob : reply[2], negative_prob : reply[1] }});
        }
    });
  }
}
