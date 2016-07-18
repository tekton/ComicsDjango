import {Component, Input, ChangeDetectionStrategy} from '@angular/core';
import {CORE_DIRECTIVES} from '@angular/common';
import {RouterLink, RouteDefinition, Router} from '@angular/router-deprecated';
import {DROPDOWN_DIRECTIVES} from "ng2-bootstrap/ng2-bootstrap"

@Component({
    selector: 'nav-bar',
    templateUrl: '/static/app/shared/nav/nav.mat.html',
    changeDetection: ChangeDetectionStrategy.OnPush,
    directives: [RouterLink, CORE_DIRECTIVES, DROPDOWN_DIRECTIVES]
})
export class NavBarComponent {
    @Input() brand: string;  // using bootstrap naming convention
    public status: { isopen: boolean } = { isopen: false };
    public disabled: boolean = false;

    constructor(private _router: Router) { };

    public toggled(open: boolean): void {
        console.log('Dropdown is now: ', open);
    }

    public toggleDropdown($event: MouseEvent): void {
        $event.preventDefault();
        $event.stopPropagation();
        this.status.isopen = !this.status.isopen;
    }

    gotoSection(route: any) {
        let link = [route];
        this._router.navigate(link);
    }
}


// import {Component} from '@angular/core';
// import { Injectable } from '@angular/core';
// import {DROPDOWN_DIRECTIVES} from "ng2-bootstrap/ng2-bootstrap"
// import {Router} from '@angular/router-deprecated';
// import {RouteParams, ROUTER_DIRECTIVES, ROUTER_PROVIDERS} from "@angular/router-deprecated";

// @Injectable()
// @Component({
//     selector: 'nav-bar',
//     templateUrl: "/static/app/shared/nav/nav.html",
//     directives: [DROPDOWN_DIRECTIVES, ROUTER_DIRECTIVES],
//     providers: [ROUTER_PROVIDERS, RouteParams],
// })
// export class NavBarComponent {
//     public disabled: boolean = false;
//     public status: { isopen: boolean } = { isopen: false };
//     public auth_items: Array<string> = ['Settings', 'Logout'];

//     constructor(private _router: Router,
//         private _routeParams: RouteParams) { }

//     public toggled(open: boolean): void {
//         console.log('Dropdown is now: ', open);
//     }

//     public toggleDropdown($event: MouseEvent): void {
//         $event.preventDefault();
//         $event.stopPropagation();
//         this.status.isopen = !this.status.isopen;
//     }

//     gotoSection(route: any) {
//         let link = [route];
//         this._router.navigate(link);
//     }

// }