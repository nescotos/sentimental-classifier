import { Component } from '@angular/core';
import {HttpService} from './services/http.service';

@Component({
  selector: 'my-app',
  templateUrl: "app/templates/app.component.html",
  providers: [HttpService]
})
export class AppComponent {
  error: string = "";
  sentence:string = "";
  prediction:string;
  prob_positive:number;
  prob_negative:number;
  constructor(public httpService: HttpService) {

  }

  public predictSentence(){
    if(this.sentence == ""){
      this.error = "Please select a non-empty sentence";
    }else{
      this.prediction = ""
      this.httpService.predictSentence(this.sentence).subscribe( response => {
        if(response['success']){
          this.prob_positive = response['results']['positive_prob'];
          this.prob_negative = response['results']['negative_prob'];
          if(response['results']['prediction'] == 1){
            this.prediction = "positive sentence";
          }else{
            this.prediction = "negative sentence";
          }
        }
      });
    }
  }

  name = 'Sentiment Analyser';
}
