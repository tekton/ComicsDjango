import {Component, Input, OnInit} from '@angular/core';
import {Hero} from './hero';
import { HeroService } from './hero.service';
import {RouteParams} from "@angular/router-deprecated";

@Component({
    selector: 'my-hero-detail',
    templateUrl: '/static/app/hero-detail.component.html'
})
export class HeroDetailComponent implements OnInit {
    @Input()
    hero: Hero;

    constructor(
        private _heroService: HeroService,
        private _routeParams: RouteParams){};

    ngOnInit() {
        let id = +this._routeParams.get('id');
        this._heroService.getHero(id)
            .then(hero => this.hero = hero);
    }

    goBack() {
        window.history.back();
    }
}