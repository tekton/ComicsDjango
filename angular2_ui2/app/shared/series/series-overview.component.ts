import {Component, Input, OnInit} from '@angular/core';
import {Series} from './series';
import { SeriesService } from './series.service';
import {RouteParams} from "@angular/router-deprecated";
import {Issue} from "../issues/issue";
import {DataTableDirectives} from 'angular2-datatable/datatable';

@Component({
    selector: 'series-list-detail',
    templateUrl: '/static/app/shared/series/series-overview.component.html',
    directives: [DataTableDirectives]
})
export class SeriesOverviewComponent implements OnInit {
    series: Series;
    issueList: Issue[];
    errorMessage: string;

    constructor(
        private _seriesService: SeriesService,
        private _routeParams: RouteParams){};

    ngOnInit() {
        console.log("series overview");
        let id = +this._routeParams.get('id');
        this.getSeries(id);
    }

    getSeries(id: number){
        console.log("getSeries");
        this._seriesService.getSeries(id)
            .subscribe(series => this.series = series,
                       error => this.errorMessage = <any>error,
                       () => this.handleData(this.series));
        this._seriesService.getIssueList(id)
            .subscribe(issueList => this.issueList = issueList,
                error => this.errorMessage = <any>error,
                () => this.handleData(this.issueList));
    }

    handleData(data: any) {
        console.log("hd", data);
    }

    goBack() {
        window.history.back();
    }
}