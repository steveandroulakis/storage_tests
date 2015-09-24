#include <stdio.h>
#include <stdlib.h>

void adx_store_data(const char *filepath, const char *data)
{
    FILE *fp = fopen(filepath, "ab");
    if (fp != NULL)
    {
        fputs(data, fp);
        fclose(fp);
    }
}

int main(int argc, char **argv)
{
	adx_store_data(argv[1], "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum tempor lobortis elementum. Praesent aliquam faucibus tincidunt. Fusce dolor ante, aliquam quis neque nec, volutpat vestibulum magna. Pellentesque eget urna ut metus auctor ornare ut nec orci. Aliquam eu fringilla tortor. Praesent mollis convallis nisi. Etiam viverra laoreet lacus, vitae tristique massa euismod sed. Suspendisse viverra mattis arcu ut venenatis. Sed eget commodo nulla. Suspendisse nec facilisis mi. Maecenas ut sapien lorem. Cras nibh arcu, eleifend at lorem ac, imperdiet vulputate nulla. Ut eu semper leo. Phasellus convallis, urna tincidunt faucibus lacinia, mi leo faucibus eros, hendrerit euismod justo elit non elit. Nunc vestibulum dui quis mollis consectetur. Etiam sodales aliquet tortor sed sodales. Suspendisse finibus tellus tempor elit interdum semper. Nam efficitur nulla quis nisl viverra ornare. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Maecenas eu ullamcorper nibh. Donec convallis, erat id finibus tristique, orci risus imperdiet odio, sed consectetur felis ligula vel felis. Aliquam erat volutpat. Duis lorem urna, condimentum vel elit et, suscipit condimentum sapien. Etiam dictum facilisis ex quis consectetur. Etiam dictum dignissim ligula id imperdiet. Mauris metus ex, bibendum ut rhoncus eget, cursus eu ex. Fusce at turpis dui. Aliquam dapibus, ex vel gravida lobortis, urna mi vulputate nibh, sed gravida ipsum est at est. Nulla augue lectus, volutpat et nulla ac, tempor hendrerit dolor. Nulla facilisi. Pellentesque in commodo massa. Maecenas tincidunt augue vitae lectus imperdiet vestibulum. Sed in egestas mi. Phasellus eu condimentum ex, sit amet euismod velit. Curabitur ipsum purus, volutpat eu tristique at, ultrices sed tellus. Fusce sed vestibulum augue. Praesent sit amet turpis mauris. Etiam ipsum purus, viverra nec pellentesque vehicula, venenatis nec nisl. Donec ex justo, malesuada vel ligula et, tincidunt volutpat diam. Aliquam et magna at nisl rhoncus imperdiet. Nulla a finibus dui. Vestibulum id finibus libero. Aenean dolor erat, pellentesque eget maximus nec, egestas at orci. Maecenas lacus orci, cursus eget tortor ac, aliquet varius ex. Fusce sapien leo, sagittis at risus ac, sodales commodo odio. Nulla dictum, quam non rhoncus mollis, massa dui lacinia purus, id tempor nibh lacus eu odio.");

    return 0;
}
