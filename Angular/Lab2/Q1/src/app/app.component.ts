import { NgModule } from '@angular/core';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
// import { HeroComponent } from './hero/hero.component';
// import { AboutComponent } from './about/about.component';
// import { SkillComponent } from './skill/skill.component';
// import { PortfolioComponent } from './portfolio/portfolio.component';
// import { FooterComponent } from './footer/footer.component';
import {UserListComponent} from './user-list/user-list.component'


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,UserListComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'angular-project';
}
