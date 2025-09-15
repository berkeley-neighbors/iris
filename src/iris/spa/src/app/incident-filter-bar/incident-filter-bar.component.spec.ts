import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IncidentFilterBarComponent } from './incident-filter-bar.component';

describe('IncidentFilterBarComponent', () => {
  let component: IncidentFilterBarComponent;
  let fixture: ComponentFixture<IncidentFilterBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IncidentFilterBarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IncidentFilterBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
