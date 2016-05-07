import {Component, Input, OnInit} from '@angular/core';
import {Thumb} from './thumb';
import { ThumbService } from './thumbs.service';
import {RouteParams} from "@angular/router-deprecated";

@Component({
    selector: 'thumb-strip',
    templateUrl: '/static/app/thumb-strip.component.html'
})
export class ThumbStripComponent implements OnInit {
    thumbList: Thumb[];
    errorMessage: string;

    constructor(
        private _pullService: ThumbService,
        private _routeParams: RouteParams){};

    ngOnInit() {
        this.getList();
    }

    getList(){
        console.log("getList");
        this._pullService.getList()
            .subscribe(list => this.thumbList = list,
                       error => this.errorMessage = <any>error);
    }

    goBack() {
        window.history.back();
    }
}