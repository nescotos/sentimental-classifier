import {Injectable} from '@angular/core'
import {Observable} from 'rxjs/Observable';
import {Http, Headers, Response} from "@angular/http";
import {Config} from '../config';
import "rxjs/add/operator/do";
import "rxjs/add/operator/map";

@Injectable()
export class HttpService {
  constructor(public http: Http) {

  }

  public predictSentence(sentence: string) {
    return new Observable(observable => {
      let headers = new Headers();
      headers.append("Content-Type", "application/json");
      this.http.post(new Config().URLSERVER + '/api/sentiment/sentence', JSON.stringify({
        sentence : sentence
      }), { headers: headers }).map(res => res.json())
        .subscribe(res => {
          if (res.code == "404" || res.code == "500") {
            console.error('Brutal error');
          } else {
            observable.next(res);
          }
        });
    });
  }
}
