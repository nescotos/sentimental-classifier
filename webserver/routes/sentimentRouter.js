var SentimentController = require('../controllers/sentimentController');

module.exports = function(express){
  var sentimentRouter = express.Router();

  sentimentRouter.route('/sentiment/sentence')
  .post(SentimentController.predictSentimentSentence);

  return sentimentRouter;
}
