import { ComponentFixture, TestBed } from '@angular/core/testing';

import { IncidentResultsTableComponent } from './incident-results-table.component';

describe('IncidentResultsTableComponent', () => {
  let component: IncidentResultsTableComponent;
  let fixture: ComponentFixture<IncidentResultsTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [IncidentResultsTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(IncidentResultsTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
