from itertools import cycle
from typing import List, Dict
from collections import defaultdict

def assign_employees_to_managers(
    managers: List[str],
    employees: List[str]
) -> Dict[str, List[str]]:
    
    manager_cycle = cycle(managers)
    
    assignments: Dict[str, List[str]] = defaultdict(list)
    
    list(map(
        lambda emp, mgr: assignments[mgr].append(emp),
        employees,
        (next(manager_cycle) for _ in employees)
    ))
    
    return {manager: sorted(employees_list) for manager, employees_list in assignments.items()}

if __name__ == "__main__":
    managers = ["Utkarsh", "Praveen", "Adithya"]
    employees = [
        "Emp1", "Emp2", "Emp3", "Emp4",
        "Emp5", "Emp6", "Emp7", "Emp8",
        "Emp9", "Emp10", "Emp11", "Emp12"
    ]
    
    reporting_structure = assign_employees_to_managers(managers, employees)
    
    print("\n\n      Employee Reporting Structure:")
    print("=" * 45)
    print("\n\n")
    for manager, team in reporting_structure.items():
        print(f"{manager} (Group Size: {len(team)})")
        for employee in team:
            print(f"    -> {employee}")
        print()