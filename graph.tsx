import React, { useState, useEffect } from 'react';
import { IndianRupee } from 'lucide-react';
import LineGraph from './components/charts/LineGraph';
import { Expense } from './types/expense';

function App() {
  const [expenses, setExpenses] = useState<Expense[]>(() => {
    const saved = localStorage.getItem('expenses');
    if (saved) {
      return JSON.parse(saved).map((expense: any) => ({
        ...expense,
        date: new Date(expense.date),
      }));
    }
    return [];
  });

  useEffect(() => {
    localStorage.setItem('expenses', JSON.stringify(expenses));
  }, [expenses]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 p-8">
      <div className="max-w-4xl mx-auto">
        <LineGraph expenses={expenses} />
      </div>
    </div>
  );
}

export default App;
