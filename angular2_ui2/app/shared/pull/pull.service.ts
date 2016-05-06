///<reference path="../../../typings/browser.d.ts"/>
import {Injectable} from "angular2/core";
import {Http, Response} from 'angular2/http';
import {Pull} from "./pull";
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class PullService {
    constructor (private http: Http) {}

    private _pullListUrl = '/pull/api/1.0/list';  // URL to web api

    getList (): Observable<Pull[]> {
        return this.http.get(this._pullListUrl)
                        .map(this.extractData)
                        .catch(this.handleError);
    }

    private extractData(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
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