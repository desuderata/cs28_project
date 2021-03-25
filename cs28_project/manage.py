#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cs28_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



                # numerical_score = [str(s) for s in numerical_score]
                # weight_list = [str(w) for w in weight_list]
                # overall_points = Decimal('0')
                # # print(numerical_score)
                # for i, j in zip(numerical_score, weight_list):
                #     overall_points += Decimal(i) * Decimal(j)
                # print(overall_points)
