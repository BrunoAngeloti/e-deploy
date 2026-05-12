from datetime import date


def calculate_resignation_benefits(
    salary: float,
    admission_date: date,
    resignation_date: date
) -> dict:
    # Calcula valores de férias proporcionais e décimo terceiro até a data de demissão
    if salary <= 0:
      raise ValueError("The salary must be greater than zero.")

    if resignation_date < admission_date:
      raise ValueError("The resignation date cannot be earlier than the admission date.")

    vacation_period_start = get_last_work_anniversary(
      admission_date=admission_date,
      reference_date=resignation_date
    )

    vacation_months = count_proportional_months(
      start_date=vacation_period_start,
      end_date=resignation_date
    )

    vacation_base_amount = salary * (vacation_months / 12)
    vacation_one_third_bonus = vacation_base_amount / 3
    total_vacation_amount = vacation_base_amount + vacation_one_third_bonus

    thirteenth_salary_period_start = max(
      admission_date,
      date(resignation_date.year, 1, 1)
    )

    thirteenth_salary_months = count_proportional_months(
      start_date=thirteenth_salary_period_start,
      end_date=resignation_date
    )

    thirteenth_salary_amount = salary * (thirteenth_salary_months / 12)

    return {
      "vacation_months": vacation_months,
      "vacation_base_amount": round(vacation_base_amount, 2),
      "vacation_one_third_bonus": round(vacation_one_third_bonus, 2),
      "total_vacation_amount": round(total_vacation_amount, 2),
      "thirteenth_salary_months": thirteenth_salary_months,
      "thirteenth_salary_amount": round(thirteenth_salary_amount, 2),
      "total_amount_to_receive": round(
          total_vacation_amount + thirteenth_salary_amount,
          2
      )
    }


def get_last_work_anniversary(admission_date: date, reference_date: date) -> date:
  # Retorna o último aniversário de trabalho antes da data de demissão
  try:
    anniversary = date(
      reference_date.year,
      admission_date.month,
      admission_date.day
    )
  except ValueError:
    anniversary = date(reference_date.year, 2, 28)

  if anniversary > reference_date:
    try:
      anniversary = date(
        reference_date.year - 1,
        admission_date.month,
        admission_date.day
      )
    except ValueError:
      anniversary = date(reference_date.year - 1, 2, 28)

  return anniversary


def count_proportional_months(start_date: date, end_date: date) -> int:
  # Conta meses proporcionais com pelo menos 15 dias trabalhados
  months = 0
  year = start_date.year
  month = start_date.month

  while (year, month) <= (end_date.year, end_date.month):
    first_day_of_month = date(year, month, 1)

    if month == 12:
      first_day_of_next_month = date(year + 1, 1, 1)
    else:
      first_day_of_next_month = date(year, month + 1, 1)

    worked_period_start = max(start_date, first_day_of_month)
    worked_period_end = min(end_date, first_day_of_next_month)

    worked_days = (worked_period_end - worked_period_start).days

    if worked_days >= 15:
      months += 1

    if month == 12:
      year += 1
      month = 1
    else:
      month += 1

  return min(months, 12)


result = calculate_resignation_benefits(
  salary=3000,
  admission_date=date(2022, 8, 10),
  resignation_date=date(2026, 5, 12)
)

print(result)