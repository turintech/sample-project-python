from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.sql.query import SqlQuery


def single():
    print("SingleForLoop")
    print("-------------")

    print(f"sum_range(10): {SingleForLoop.sum_range(10)}")
    print(f"max_list([1, 2, 3]): {SingleForLoop.max_list([1, 2, 3])}")
    print(f"sum_modulus(100, 3): {SingleForLoop.sum_modulus(100, 3)}")
    print()


def double():
    print("DoubleForLoop")
    print("-------------")

    print(f"sum_square(10): {DoubleForLoop.sum_square(10)}")
    print(f"sum_triangle(10): {DoubleForLoop.sum_triangle(10)}")
    print(
        f"count_pairs(random_list(30, 10)): {DoubleForLoop.count_pairs(GenList.random_list(30, 10))}"
    )
    print(
        "count_duplicates(10, 10)",
        DoubleForLoop.count_duplicates(
            GenList.random_list(10, 2), GenList.random_list(10, 2)
        ),
    )
    print(
        f"sum_matrix(random_matrix(10, 10)): {DoubleForLoop.sum_matrix(GenList.random_matrix(10, 10))}"
    )
    print()


def sql():
    print("SQL")
    print("---")

    print(f"query_album('Presence'): {SqlQuery.query_album('Presence')}")
    print(f"query_album('Roundabout'): {SqlQuery.query_album('Roundabout')}")
    print()

    print("join_albums()")
    print(SqlQuery.join_albums()[0])
    print()

    print("top_invoices()")
    print(SqlQuery.top_invoices())
    print()


def main():
    single()
    double()
    sql()


if __name__ == "__main__":
    main()
