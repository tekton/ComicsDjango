///<reference path="../../../typings/browser.d.ts"/>
import {Injectable} from "@angular/core";
import {Http, Response} from '@angular/http';
import {Series} from "./series";
import {Observable}     from 'rxjs/Observable';
import {Issue} from "../issues/issue";

@Injectable()
export class SeriesService {
    constructor (private http: Http) {}
    private _seriesUrl = "/_comics/api/1.0/series";
    private _issuesUrl = "/_issues/api/1.0/series_issues";

    getList (): Observable<Series[]> {
        return this.http.get(this._seriesUrl)
            .map(this.extractData)
            .catch(this.handleError);
    }

    getSeries(id: number):Observable<Series> {
        return this.http.get(this._seriesUrl + "/" + id)
            .map(this.extractData)
            .catch(this.handleError);
    }

    getIssueList(id: number):Observable<Issue[]> {
        return this.http.get(this._issuesUrl + "/" + id)
            .map(this.extractData)
            .catch(this.handleError);
    }

    private extractData(res: Response) {
        if (res.status < 200 || res.status >= 300) {
            throw new Error('Bad response status: ' + res.status);
        } else {
            console.log("series resp", res);
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