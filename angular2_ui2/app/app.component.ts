import { Component }       from '@angular/core';
import {PullListComponent} from "./shared/pull/pull-list.component";
import {PullService} from "./shared/pull/pull.service";
import {ThumbService} from "./shared/thumbs/thumbs.service";
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from '@angular/router-deprecated';
import {DashboardComponent} from "./dashboard.component";

@Component({
    selector: 'my-app',
    templateUrl: '/static/app/base.html',
    directives: [ROUTER_DIRECTIVES],
    providers: [
        ROUTER_PROVIDERS,
        PullService,
        ThumbService
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
    }
])
export class AppComponent {
    title = 'Angular UI Test Title Area';
}