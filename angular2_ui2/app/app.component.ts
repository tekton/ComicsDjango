import { Component }       from 'angular2/core';
import { HeroService }     from './shared/heroes/hero.service';
import { HeroesComponent } from './shared/heroes/heroes.component';
import {PullListComponent} from "./shared/pull/pull-list.component";
import {PullService} from "./shared/pull/pull.service";
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';
import {DashboardComponent} from "./dashboard.component";
import {HeroDetailComponent} from "./shared/heroes/hero-detail.component";

@Component({
    selector: 'my-app',
    template: `
        <h1>{{title}}</h1>
        <nav>
            <a [routerLink]="['Dashboard']">Dashboard</a>
            <a [routerLink]="['Heroes']">Heroes</a>
            <a [routerLink]="['Pulls']">Pulls</a>
        </nav>
        <router-outlet></router-outlet>
  `,
    directives: [ROUTER_DIRECTIVES],
    providers: [
        ROUTER_PROVIDERS,
        HeroService,
        PullService
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
        component: DashboardComponent
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