import { Component }       from '@angular/core';
import { HeroService }     from './shared/heroes/hero.service';
import { HeroesComponent } from './shared/heroes/heroes.component';
import {PullListComponent} from "./shared/pull/pull-list.component";
import {PullService} from "./shared/pull/pull.service";
import {ThumbService} from "./shared/thumbs/thumbs.service";
import {ThumbStripComponent} from "./shared/thumbs/thumbs.component";
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from '@angular/router-deprecated';
import {DashboardComponent} from "./dashboard.component";
import {HeroDetailComponent} from "./shared/heroes/hero-detail.component";

@Component({
    selector: 'my-app',
    template: `
        <h1>{{title}}</h1>
        <nav>
            <a [routerLink]="['Dashboard']">Dashboard</a>
            <a [routerLink]="['Pulls']">Pulls</a>
        </nav>
        <router-outlet></router-outlet>
  `,
    directives: [ROUTER_DIRECTIVES],
    providers: [
        ROUTER_PROVIDERS,
        HeroService,
        PullService,
        ThumbService
    ]
})
@RouteConfig([
    {
        path: '/heroes',
        name: 'Heroes',
        component: HeroesComponent
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: ThumbStripComponent
    },
    {
        path: '/pulls',
        name: 'Pulls',
        component: PullListComponent,
        useAsDefault: true
    },
    {
        path: '/detail/:id',
        name: 'HeroDetail',
        component: HeroDetailComponent
    }
])
export class AppComponent {
    title = 'Angular UI Test Title Area';
}