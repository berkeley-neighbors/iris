import { Routes } from '@angular/router';
import { IncidentPageComponent } from './incident-page/incident-page.component';

export const routes: Routes = [{
    path: '',
    component: IncidentPageComponent
},
{
    path: 'incidents',
    component: IncidentPageComponent
}];
