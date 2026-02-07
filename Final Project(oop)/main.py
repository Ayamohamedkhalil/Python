

from Person import person
from Employee import Employee
from Car import Car
from Office import Office


def main():

    print("=" * 70)
    print("  SAMY'S DAILY ROUTINE - OOP DEMONSTRATION")
    print("=" * 70)

    # Create ITI Office
    print("\n1. CREATING ITI OFFICE")
    print("-" * 70)
    iti = Office("ITI Smart Village")
    print(f"Created office: {iti}")

    # Create Samy's car - Fiat 128
    print("\n2. CREATING SAMY'S CAR")
    print("-" * 70)
    fiat128 = Car(name="Fiat 128", fuelRate=100, velocity=0)
    print(f"Created car: {fiat128}")

    # Create Samy as an Employee
    print("\n3. CREATING SAMY AS EMPLOYEE")
    print("-" * 70)
    samy = Employee(
        name="Samy",
        emp_id="E001",
        email="samy@iti.gov.eg",
        salary=10000,
        distanceToWork=20,
        car=fiat128,
        money=5000
    )
    print(f"Created employee: {samy}")

    # Hire Samy
    print("\n4. HIRING SAMY AT ITI")
    print("-" * 70)
    iti.hire(samy)

    # Samy's morning routine
    print("\n5. SAMY'S MORNING ROUTINE")
    print("-" * 70)
    samy.sleep(7)
    samy.eat(3)

    # Samy goes to work
    print("\n6. SAMY DRIVES TO WORK")
    print("-" * 70)
    print(f"Distance to ITI: {samy.distanceToWork} km")

    moveHour = 8.0
    velocity = 60

    print(f"\nSamy leaves home at {Office._format_time(moveHour)}")
    print(f"Driving at {velocity} km/h")

    # Check lateness
    print("\n7. CHECKING LATENESS")
    print("-" * 70)
    samy.car.velocity = velocity
    iti.check_lateness(samy.id, moveHour)

    # Drive to work
    print("\n8. DRIVING TO ITI")
    print("-" * 70)
    samy.drive(distance=samy.distanceToWork, velocity=velocity)

    # Samy works
    print("\n9. WORKING AT ITI")
    print("-" * 70)
    samy.work(8)

    # Send email
    print("\n10. SENDING EMAIL")
    print("-" * 70)
    samy.send_mail(
        to_email="hr@iti.gov.eg",
        subject="Daily Report",
        message="Completed all tasks for today successfully!"
    )

    # Refuel
    print("\n11. REFUELING CAR")
    print("-" * 70)
    print(f"Current fuel: {samy.car.fuelRate}%")
    samy.refuel(100)

    # Drive back home
    print("\n12. DRIVING BACK HOME")
    print("-" * 70)
    samy.drive(distance=20, velocity=60)

    # Evening routine
    print("\n13. EVENING ROUTINE")
    print("-" * 70)
    samy.eat(2)
    samy.buy(5)

    # Final status
    print("\n14. FINAL STATUS")
    print("-" * 70)
    print(f"Samy: {samy}")
    print(f"Car: {samy.car}")
    print(f"Office: {iti}")
    print(f"Total employees in all offices: {Office.employeesNum}")

    print("\n" + "=" * 70)
    print("  DEMONSTRATION COMPLETE!")
    print("=" * 70)


if __name__ == "__main__":
    main()
