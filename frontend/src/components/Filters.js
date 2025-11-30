import React from 'react';

const Filters = ({ options, filters, onChange }) => (
  <div className="card mb-4">
    <div className="card-header d-flex justify-content-between">
      <span>🔍 Filters</span>
      <button className="btn btn-sm btn-outline-secondary" onClick={() => onChange({})}>Clear All</button>
    </div>
    <div className="card-body">
      <div className="row g-3">
        <div className="col-md-3">
          <select 
            className="form-select" 
            value={filters.topic || ''} 
            onChange={e => onChange({...filters, topic: e.target.value, page: 1})}
          >
            <option value="">All Topics</option>
            {options.topics?.map(t => <option key={t} value={t}>{t}</option>)}
          </select>
        </div>
        <div className="col-md-3">
          <select 
            className="form-select" 
            value={filters.region || ''} 
            onChange={e => onChange({...filters, region: e.target.value, page: 1})}
          >
            <option value="">All Regions</option>
            {options.regions?.map(r => <option key={r} value={r}>{r}</option>)}
          </select>
        </div>
        <div className="col-md-2">
          <input 
            type="number" 
            className="form-control" 
            placeholder="Page" 
            value={filters.page} 
            onChange={e => onChange({...filters, page: e.target.value})}
          />
        </div>
      </div>
    </div>
  </div>
);

export default Filters;