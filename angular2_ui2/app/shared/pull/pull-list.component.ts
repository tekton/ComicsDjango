import {Component, Input, OnInit} from '@angular/core';
import {Pull} from './pull';
import { PullService } from './pull.service';
import {RouteParams} from "@angular/router-deprecated";
import {Router} from "@angular/router-deprecated";
import {ThumbStripComponent} from "../thumbs/thumbs.component";

@Component({
    selector: 'pull-list-detail',
    templateUrl: '/static/app/shared/pull/pull-list.component.html'
})
export class PullListComponent implements OnInit {
    pullList: Pull[];
    errorMessage: string;

    constructor(
        private _pullService: PullService,
        private _router: Router,
        private _routeParams: RouteParams){};

    ngOnInit() {
        this.getList();
    }

    getList(){
        console.log("getList");
        this._pullService.getList()
            .subscribe(list => this.pullList = list,
                       error => this.errorMessage = <any>error);
    }

    tup(series: number) {
        console.log(series);
        alert("TODO: Queue Transfer Primaries");
    }

    removePull(pullId: number) {
        // call the service to remove the thing...
        this._pullService.remove(pullId)
            .subscribe(data => this.handleData(data),
                       error => this.errorMessage = <any>error,
                       () => this.getList());
    }

    gotoOverview(series: number) {
        let link = ['SeriesOverview', { id: series }];
        this._router.navigate(link);
    }

    handleData(data: any) {
        console.log("hd", data);
    }

    goBack() {
        window.history.back();
    }
}