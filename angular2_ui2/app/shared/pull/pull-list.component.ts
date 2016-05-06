import {Component, Input, OnInit} from 'angular2/core';
import {Pull} from './pull';
import { PullService } from './pull.service';
import {RouteParams} from "angular2/router";

@Component({
    selector: 'pull-list-detail',
    templateUrl: '/static/app/pull-list.component.html'
})
export class PullListComponent implements OnInit {
    pullList: Pull[];
    errorMessage: string;

    constructor(
        private _pullService: PullService,
        private _routeParams: RouteParams){};

    ngOnInit() {
        this.getList();
    }

    getList(){
        this._pullService.getList()
            .subscribe(list => this.pullList = list,
                       error => this.errorMessage = <any>error);
    }

    goBack() {
        window.history.back();
    }
}