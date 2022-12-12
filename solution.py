def to_jaden_case(string):
    ans=''
    k=string.split()
    for i in k:
        ans+=i.capitalize()+' '
    return(ans[0:len(ans)-1])
  
  
import codewars_test as test


@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
