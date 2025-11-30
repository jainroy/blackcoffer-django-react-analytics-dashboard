import React from 'react';

const Table = ({ entries, page, pageSize, totalCount, onPageChange }) => {
  const totalPages = Math.ceil(totalCount / pageSize) || 1;
  const safePage = Math.max(1, Math.min(page, totalPages));
  
  return (
    <div className="card shadow">
      <div className="card-header bg-dark text-white d-flex justify-content-between">
        <h6 className="mb-0">📋 Data Table</h6>
        <span>{totalCount} total records | Page {safePage} of {totalPages}</span>
      </div>
      <div className="card-body p-0">
        <div className="table-responsive">
          <table className="table table-hover mb-0">
            <thead className="table-dark">
              <tr>
                <th style={{width: '60px'}}>ID</th>
                <th>Title</th>
                <th style={{width: '100px'}}>Topic</th>
                <th style={{width: '80px'}}>Intensity</th>
                <th style={{width: '80px'}}>Likelihood</th>
                <th>Region</th>
              </tr>
            </thead>
            <tbody>
              {entries.map(entry => (
                <tr key={entry.id}>
                  <td><strong>{entry.id}</strong></td>
                  <td className="text-truncate" style={{maxWidth: '250px'}} title={entry.title}>
                    {entry.title}
                  </td>
                  <td><span className="badge bg-primary">{entry.topic}</span></td>
                  <td><strong>{entry.intensity || '-'}</strong></td>
                  <td>{entry.likelihood || '-'}</td>
                  <td>{entry.region}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {totalPages > 1 && (
          <div className="card-footer d-flex justify-content-between align-items-center">
            <button 
              className="btn btn-outline-primary btn-sm" 
              disabled={safePage <= 1}
              onClick={() => onPageChange(safePage - 1)}
            >
              ← Previous
            </button>
            <span className="text-muted mx-3">
              Page {safePage} of {totalPages}
            </span>
            <button 
              className="btn btn-primary btn-sm" 
              disabled={safePage >= totalPages}
              onClick={() => onPageChange(safePage + 1)}
            >
              Next →
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Table;