import {Component, Input, OnInit} from '@angular/core';
import {Series} from './series';
import { SeriesService } from './series.service';
import {RouteParams} from "@angular/router-deprecated";

@Component({
    selector: 'series-list-detail',
    templateUrl: '/static/app/shared/series/series-overview.component.html'
})
export class SeriesOverviewComponent implements OnInit {
    series: Series;
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
    }

    handleData(data: any) {
        console.log("hd", data);
    }

    goBack() {
        window.history.back();
    }
}