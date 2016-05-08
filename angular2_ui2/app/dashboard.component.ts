import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router-deprecated';

import { Hero } from './shared/heroes/hero';
import { HeroService } from './shared/heroes/hero.service';

import {ThumbStripComponent} from "./shared/thumbs/thumbs.component";
import {PullListComponent} from "./shared/pull/pull-list.component"

@Component({
    selector: 'my-dashboard',
    templateUrl: '/static/app/dashboard.component.html',
    directives: [ThumbStripComponent, PullListComponent]
})
export class DashboardComponent implements OnInit {
    constructor(
        private _router: Router) { }
    ngOnInit() {
        console.log("dashboard...");
    }
}
