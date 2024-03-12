import { Component } from '@angular/core';
import {RouterModule, RouterOutlet} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterModule, HomeComponent, AboutComponent, RouterOutlet], // we add RouterModule to implement routers methods, [routerLink] in the html file
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
}
