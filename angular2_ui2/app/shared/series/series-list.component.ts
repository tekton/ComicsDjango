import {Component, Input, OnInit} from '@angular/core';
import {Series} from './series';
import { SeriesService } from './series.service';
import {RouteParams} from "@angular/router-deprecated";
import {Router} from "@angular/router-deprecated";
import {DataTableDirectives} from 'angular2-datatable/datatable';
import {MD_CARD_DIRECTIVES} from '@angular2-material/card';
import {MdButton} from '@angular2-material/button';
// @angular2-material/core
// @angular2-material/card

@Component({
    selector: 'series-list-detail',
    templateUrl: '/static/app/shared/series/series-list.component.html',
    directives: [DataTableDirectives, MD_CARD_DIRECTIVES, MdButton]
})
export class SeriesListComponent implements OnInit {
    seriesList: Series[];
    errorMessage: string;

    constructor(
        private _seriesService: SeriesService,
        private _router: Router){};

    ngOnInit() {
        console.log("series list");
        this.getList();
    }

    getList(){
        console.log("getList");
        this._seriesService.getList()
            .subscribe(list => this.seriesList = list,
                       error => this.errorMessage = <any>error);
    }

    handleData(data: any) {
        console.log("hd", data);
    }

    gotoOverview(series: Series) {
        let link = ['SeriesOverview', { id: series.id }];
        this._router.navigate(link);
    }

    goBack() {
        window.history.back();
    }
}