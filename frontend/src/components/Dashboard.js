import React, { useState, useEffect, useCallback } from 'react';
import {
  fetchEntries, fetchFilters, fetchIntensityByYear, fetchLikelihoodTrend
} from '../services/api';
import Filters from './Filters';
import BarChart from './Charts/BarChart';
import LineChart from './Charts/LineChart';
import PieChart from './Charts/PieChart';
import ScatterChart from './Charts/ScatterChart';
import Table from './Table';

const Dashboard = () => {
  const [filters, setFilters] = useState({ page: 1, pageSize: 10 });
  const [options, setOptions] = useState({});
  const [entries, setEntries] = useState([]);
  const [totalCount, setTotalCount] = useState(0);
  const [intensityData, setIntensityData] = useState([]);
  const [likelihoodData, setLikelihoodData] = useState([]);
  const [loading, setLoading] = useState(true);

  // ✅ FIXED: useCallback for loadData
  const loadData = useCallback(() => {
    setLoading(true);
    Promise.all([
      fetchEntries(filters),
      fetchIntensityByYear(),
      fetchLikelihoodTrend()
    ]).then(([entriesRes, intensityRes, likelihoodRes]) => {
      setEntries(entriesRes.data.results || []);
      setTotalCount(entriesRes.data.count || 0);
      setIntensityData(intensityRes.data || []);
      setLikelihoodData(likelihoodRes.data || []);
      setLoading(false);
    }).catch(() => setLoading(false));
  }, [filters]);

  // ✅ FIXED: Dependencies correct now
  useEffect(() => {
    fetchFilters().then(res => setOptions(res.data));
  }, []);

  useEffect(() => {
    loadData();
  }, [loadData]);

  if (loading) return <div className="container mt-5"><div className="alert alert-info text-center">Loading dashboard...</div></div>;

  return (
    <div className="container-fluid py-4" style={{backgroundColor: '#f8f9fa'}}>
      <h1 className="mb-4 text-center text-primary fw-bold">📊 Analytics Dashboard</h1>
      <div className="row mb-4">
        <div className="col-12">
          <Filters options={options} filters={filters} onChange={setFilters} />
        </div>
      </div>
      
      <div className="row g-4 mb-4">
        <div className="col-lg-6">
          <div className="card h-100 shadow">
            <div className="card-header bg-primary text-white">
              <h6 className="mb-0">📈 Average Intensity by Year ({intensityData.length} years)</h6>
            </div>
            <div className="card-body p-3" style={{minHeight: "420px"}}>
              {intensityData.length ? (
                <BarChart data={intensityData} />
              ) : (
                <div className="d-flex h-100 align-items-center justify-content-center">
                  <span className="text-muted">No intensity data available</span>
                </div>
              )}
            </div>
          </div>
        </div>
        
        <div className="col-lg-6">
          <div className="card h-100 shadow">
            <div className="card-header bg-success text-white">
              <h6 className="mb-0">📉 Likelihood Trend ({likelihoodData.length} years)</h6>
            </div>
            <div className="card-body p-3" style={{minHeight: "420px"}}>
              {likelihoodData.length ? (
                <LineChart data={likelihoodData} />
              ) : (
                <div className="d-flex h-100 align-items-center justify-content-center">
                  <span className="text-muted">No likelihood data available</span>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-6">
          <div className="card h-100 shadow">
            <div className="card-header bg-warning text-dark">
              <h6 className="mb-0">🥧 Topics Distribution ({entries.length} entries)</h6>
            </div>
            <div className="card-body p-3" style={{minHeight: "420px"}}>
              {entries.length ? <PieChart data={entries} /> : <p className="text-muted text-center mt-5">No data</p>}
            </div>
          </div>
        </div>
        
        <div className="col-lg-6">
          <div className="card h-100 shadow">
            <div className="card-header bg-info text-white">
              <h6 className="mb-0">🎯 Relevance vs Intensity (by Region)</h6>
            </div>
            <div className="card-body p-3" style={{minHeight: "420px"}}>
              {entries.length ? <ScatterChart data={entries} /> : <p className="text-muted text-center mt-5">No data</p>}
            </div>
          </div>
        </div>
      </div>

      <div className="row">
        <div className="col-12">
          <Table 
            entries={entries} 
            page={filters.page} 
            pageSize={filters.pageSize} 
            totalCount={totalCount} 
            onPageChange={(page) => setFilters(prev => ({...prev, page}))}
          />
        </div>
      </div>

      <div className="row mt-4">
        <div className="col-12 text-center">
          <small className="text-muted">
            Built with Django REST + React + Chart.js |{' '}
            <a href="http://127.0.0.1:8000/api/" target="_blank" rel="noopener noreferrer">
              API
            </a>
          </small>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;