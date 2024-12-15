import React, { useState, useEffect } from 'react';
import { IndianRupee } from 'lucide-react';
import ExpenseForm from './components/ExpenseForm';
import ExpenseChart from './components/ExpenseChart';
import MonthlyReviewCard from './components/MonthlyReviewCard';
import { Expense } from './types/expense';
import { generateMonthlyReview } from './utils/expenseUtils';

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

  const handleAddExpense = (newExpense: Omit<Expense, 'id'>) => {
    const expense: Expense = {
      ...newExpense,
      id: crypto.randomUUID(),
    };
    setExpenses((prev) => [...prev, expense]);
  };

  const monthlyReview = generateMonthlyReview(expenses);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <header className="bg-gradient-to-r from-blue-600 to-indigo-600 text-white py-6 shadow-lg">
        <div className="container mx-auto px-4">
          <div className="flex items-center space-x-3">
            <IndianRupee className="w-8 h-8" />
            <h1 className="text-2xl font-bold">Student Expense Tracker</h1>
          </div>
          <p className="mt-2 text-blue-100 ml-11">Track, Analyze, and Save Money</p>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div className="space-y-8">
            <ExpenseForm onAddExpense={handleAddExpense} />
            <MonthlyReviewCard review={monthlyReview} />
          </div>
          <div className="space-y-8">
            <ExpenseChart expenses={expenses} />
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
