///<reference path="../../../typings/browser.d.ts"/>
import {Injectable} from "@angular/core";
import {Http, Response} from '@angular/http';
import {Thumb} from "./thumb";
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class ThumbService {
    constructor (private http: Http) {}
    private _thumbsUrl = "/comics/api/1.0/thumbnails/4";

    getList (): Observable<Thumb[]> {
        return this.http.get(this._thumbsUrl+"/10")
            .map(this.extractData)
            .catch(this.handleError);
    }

    private extractData(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        } else {
            console.log("thumb resp", res);
        }
        let body = res.json();
        console.log(body);
        return body || { };
    }

    private handleError(error: any) {
        let errMsg = error.message || 'Server error';
        console.error(errMsg); // log to console instead
        return Observable.throw(errMsg);
    }
}