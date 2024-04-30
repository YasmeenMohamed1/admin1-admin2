/// <reference types="@angular/localize" />

import { HeroComponent } from './app/hero/hero.component';
// import { SkillComponent } from './app/skill/skill.component';
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
// import { SkillsComponentComponent } from './app/skills-component/skills-component.component';


bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
