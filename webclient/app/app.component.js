"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var http_service_1 = require('./services/http.service');
var AppComponent = (function () {
    function AppComponent(httpService) {
        this.httpService = httpService;
        this.error = "";
        this.sentence = "";
        this.name = 'Sentiment Analyser';
    }
    AppComponent.prototype.predictSentence = function () {
        var _this = this;
        if (this.sentence == "") {
            this.error = "Please select a non-empty sentence";
        }
        else {
            this.prediction = "";
            this.httpService.predictSentence(this.sentence).subscribe(function (response) {
                if (response['success']) {
                    _this.prob_positive = response['results']['positive_prob'];
                    _this.prob_negative = response['results']['negative_prob'];
                    if (response['results']['prediction'] == 1) {
                        _this.prediction = "positive sentence";
                    }
                    else {
                        _this.prediction = "negative sentence";
                    }
                }
            });
        }
    };
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            templateUrl: "app/templates/app.component.html",
            providers: [http_service_1.HttpService]
        }), 
        __metadata('design:paramtypes', [http_service_1.HttpService])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map