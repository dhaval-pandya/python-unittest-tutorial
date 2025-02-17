import unittest

def raises_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))

class ExceptionTest(unittest.TestCase):

    def test_trap_locally(self):
        try:
            #raises_error('a', b='c')
            pass
        except ValueError:
            pass
        else:
            #self.fail('Did not see ValueError')
            pass

    def test_assert_raises(self):
        #self.assertRaises(ValueError, raises_error, 'a', b='c')
        pass

if __name__ == '__main__':
    unittest.main()
