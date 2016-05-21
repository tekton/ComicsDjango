import { Component }       from '@angular/core';
import {PullListComponent} from "./shared/pull/pull-list.component";
import {PullService} from "./shared/pull/pull.service";
import {ThumbService} from "./shared/thumbs/thumbs.service";
import { RouteConfig, RouteDefinition, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from '@angular/router-deprecated';
import {DashboardComponent} from "./dashboard.component";
import {SeriesListComponent} from "./shared/series/series-list.component";
import {SeriesService} from "./shared/series/series.service";
import {SeriesOverviewComponent} from "./shared/series/series-overview.component";
import {NavBarComponent} from "./shared/nav/nav.component";
import {SeriesNewComponent} from "./shared/series/series-new.component";

@Component({
    selector: 'my-app',
    templateUrl: '/static/app/base.html',
    directives: [ROUTER_DIRECTIVES, NavBarComponent],
    providers: [
        ROUTER_PROVIDERS,
        PullService,
        ThumbService,
        SeriesService
    ]
})
@RouteConfig([
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: DashboardComponent,
        useAsDefault: true
    },
    {
        path: '/pulls',
        name: 'Pulls',
        component: PullListComponent
    },
    {
        path: '/series',
        name: 'Series',
        component: SeriesListComponent
    },
    {
        path: '/series/new',
        name: 'SeriesNew',
        component: SeriesNewComponent
    },
    {
        path: '/series/:id',
        name: 'SeriesOverview',
        component: SeriesOverviewComponent
    }
])
export class AppComponent {
    public appRoutes: RouteDefinition[];
    title = 'Angular UI Test Title Area';
}