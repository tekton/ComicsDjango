import {Component, Input, OnInit} from '@angular/core';
import {Thumb} from './thumb';
import { ThumbService } from './thumbs.service';
import {RouteParams} from "@angular/router-deprecated";

@Component({
    selector: 'thumb-strip',
    templateUrl: '/static/app/shared/thumbs/thumb-strip.component.html'
}) //hope
export class ThumbStripComponent implements OnInit {
    thumbList: Thumb[];
    errorMessage: string;

    constructor(
        private _pullService: ThumbService,
        private _routeParams: RouteParams){
        console.log("oh hai thumbs");
    };

    ngOnInit() {
        console.log("thumb init");
        this.getList();
    }

    getList(){
        console.log("getThumbList");
        this._pullService.getList()
            .subscribe(list => this.thumbList = list,
                       error => this.errorMessage = <any>error);
    }

    goBack() {
        window.history.back();
    }
}